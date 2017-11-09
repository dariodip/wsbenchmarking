from flask import Flask, jsonify, render_template
from utils import fibonacci
from data import models, db


app = Flask(__name__, static_url_path='/static')
db_source = db.db_source


@app.route('/api/hello_world', methods=['GET'])
def hello():
    return jsonify({'hello': 'World'})


@app.route('/api/hello/<user>', methods=['GET'])
def hello_user(user: str):
    return jsonify({'hello': '{}'.format(user)})


@app.route('/api/fib30', methods=['GET'])
def fib30():
    return jsonify({'fibonacci30': fibonacci.fibonacci(30)})


@app.route('/api/single_user', methods=['GET'])
def single_user():
    user = db.session.query(models.Person).first()
    return jsonify({'user': models.__get_user(user)})


@app.route('/api/all_users', methods=['GET'])
def all_users():
    users = [models.__get_user(u) for u in db.session.query(models.Person).all()]
    return jsonify({'users': users})


@app.route('/api/users_with_cities', methods=['GET'])
def usrs_w_cities():
    u_w_c = db.session.query(models.Person, models.City).filter(models.Person.city_id == models.City.id).all()
    return jsonify({'users_with_cities': [models.__get_user_w_city(u) for u in u_w_c]})


@app.route('/hello_page')
def hello_page():
    return render_template('hello_page.html')


@app.route('/hello/<user>')
def hello_user_page(user: str):
    return render_template('hello_name.html', name=user)


@app.route('/fib30')
def fib30_page():
    return render_template('fib30.html', fib=fibonacci.fibonacci(30))

@app.route('/single_user', methods=['GET'])
def single_user_page():
    user = db.session.query(models.Person).first()
    return render_template('/single_user.html', user=user)


@app.route('/all_users', methods=['GET'])
def all_users_page():
    users = [models.__get_user(u) for u in db.session.query(models.Person).all()]
    print(users[0].keys())
    return render_template('/all_users.html', users=users)


@app.route('/users_with_cities', methods=['GET'])
def usrs_w_cities_page():
    u_w_c = db.session.query(models.Person, models.City).filter(models.Person.city_id == models.City.id).all()
    els = [models.__get_user_w_city(u) for u in u_w_c]
    return render_template('/all_users_w_city.html', els=els)

if __name__ == '__main__':
    app.run()
