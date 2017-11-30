from flask import Blueprint, render_template
from data import models, db
from utils import fibonacci


pages_routes = Blueprint('pages', __name__)


@pages_routes.route('/hello_world')
def hello_page():
    return render_template('hello_page.html')


@pages_routes.route('/hello/<user>')
def hello_user_page(user: str):
    return render_template('hello_name.html', name=user)


@pages_routes.route('/fib30')
def fib30_page():
    return render_template('fib30.html', fib=fibonacci.fibonacci(30))


@pages_routes.route('/single_user', methods=['GET'])
def single_user_page():
    user = db.session.query(models.Person).first()
    return render_template('/single_user.html', user=user)


@pages_routes.route('/all_users', methods=['GET'])
def all_users_page():
    users = [models.__get_user(u) for u in db.session.query(models.Person).all()]
    print(users[0].keys())
    return render_template('/all_users.html', users=users)


@pages_routes.route('/users_with_cities', methods=['GET'])
def usrs_w_cities_page():
    u_w_c = db.session.query(models.Person, models.City).filter(models.Person.city_id == models.City.id).all()
    els = [models.__get_user_w_city(u) for u in u_w_c]
    return render_template('/all_users_w_city.html', els=els)
