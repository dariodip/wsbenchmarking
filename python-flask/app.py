from flask import Flask, jsonify
from utils import fibonacci
from data import models, db


app = Flask(__name__)
db_source = db.db_source


@app.route('/hello_world', methods=['GET'])
def hello():
    return jsonify({'hello': 'World'})


@app.route('/hello/<user>', methods=['GET'])
def hello_user(user: str):
    return jsonify({'hello': '{}'.format(user)})


@app.route('/fib30', methods=['GET'])
def fib30():
    return jsonify({'fibonacci30': fibonacci.fibonacci(30)})


@app.route('/single_user', methods=['GET'])
def single_user():
    user = db.session.query(models.Person).first()
    return jsonify({'user': models.__get_user(user)})


@app.route('/all_users', methods=['GET'])
def all_users():
    users = [models.__get_user(u) for u in db.session.query(models.Person).all()]
    return jsonify({'users': users})


@app.route('/users_with_cities', methods=['GET'])
def usrs_w_cities():
    u_w_c = db.session.query(models.Person, models.City).filter(models.Person.city_id == models.City.id).all()
    return jsonify({'users_with_cities': [models.__get_user_w_city(u) for u in u_w_c]})


if __name__ == '__main__':
    app.run()
