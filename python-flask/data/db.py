from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_source = create_engine('sqlite:///db.sqlitedb', echo=False)
DBSession = sessionmaker(bind=db_source)
session = DBSession()
