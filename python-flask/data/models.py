from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    post_code = Column(String(250), nullable=False)
    region = Column(String(250), nullable=True)


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    city_id = Column(Integer, ForeignKey('city.id'))
    city = relationship(City)


def __get_user_w_city(u_w_c):
    return {'user': __get_user(u_w_c.Person), 'city': __get_city(u_w_c.City)}


def __get_city(city):
    return {'name': city.name, 'post_code': city.post_code, 'id': city.id, 'region': city.region}


def __get_user(user):
    return {'name': user.name, 'surname': user.surname, 'id': user.id, 'city': user.city_id}



