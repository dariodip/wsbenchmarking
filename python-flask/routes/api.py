from flask import Blueprint, jsonify
from data import models, db
from utils import fibonacci


api_routes = Blueprint('api', __name__)


@api_routes.route('/api/hello_world', methods=['GET'])
def hello():
    return jsonify({'hello': 'World'})


@api_routes.route('/api/hello/<user>', methods=['GET'])
def hello_user(user: str):
    return jsonify({'hello': '{}'.format(user)})


@api_routes.route('/api/fib30', methods=['GET'])
def fib30():
    return jsonify({'fibonacci30': fibonacci.fibonacci(30)})


@api_routes.route('/api/single_user', methods=['GET'])
def single_user():
    user = db.session.query(models.Person).first()
    return jsonify({'user': models.__get_user(user)})


@api_routes.route('/api/all_users', methods=['GET'])
def all_users():
    users = [models.__get_user(u) for u in db.session.query(models.Person).all()]
    return jsonify({'users': users})


@api_routes.route('/api/users_with_cities', methods=['GET'])
def usrs_w_cities():
    u_w_c = db.session.query(models.Person, models.City).filter(models.Person.city_id == models.City.id).all()
    return jsonify({'users_with_cities': [models.__get_user_w_city(u) for u in u_w_c]})
