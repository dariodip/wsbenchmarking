# restbenchmarking
Benchmarking of a simple web server developed using different programming languages and frameworks.

This project was developed for the project of Wireless Networks at Università degli Studi di Salerno.

In this project we developed two WSs having the same API and, as far as possible, the same structure. We did a simple benchmark on both these WSs in order to retrieve their efficiency on different scenarios.

The purpose of this project was to compare the efficiency between different web servers on small projects (e.g. to be used for microservice development). 

## Project structure

We implemented the same API both on [Python's Flask](http://flask.pocoo.org/) and in [Node.js' Express](http://expressjs.com/).

Both the WSs use an SQLite database preloaded with data generated from [Generate Data](https://www.generatedata.com/). The db has the following tables:

- `city(id, name, post_code, region)`: contains 300 cities;
- `person(id, name, surname, city_id)`: contains 1000 persons. `city_id` is the foreign key for `id` of the table `city`.

Both the WSs retrieve data from the external source [JSONPlaceholder](https://jsonplaceholder.typicode.com/). The retrieved data have the following schema:

-`post(userId, id, title, body)`;
-`album(userId, id, title)`;
-`photo(albumId, id, title, url, thumbnailUrl)`.

### Python Flask

In the folder `python-flask` there is the WS developed in Python. 

The WS has been developed using [Python 3.6](https://www.python.it/), [Flask 0.12.0](http://flask.pocoo.org/docs/0.12/) as a webdevelopment framework and [SQLAlchemy 1.1.14](https://www.sqlalchemy.org/) as ORM.

#### Setup

In order to install the WS and all his requirements you have to create a virtual environment using [venv](https://virtualenv.pypa.io/en/stable/) on Python 3.6.
To install *virtualenv*, run the following:

`[sudo] pip3 install virtualenv` on Linux/MacOS
or
`pip install virtualenv` using prompt as administrator on Windows.

To create a virtual environment, in the main directory of the project run:

`virtualenv venv`.

To activate the virtual environment in the directory `\venv`, in the main directory on the project run:

`source venv/bin/activate` on Linux/MacOS
or
`venv\Scripts\activate` on Windows.

You can check if the virtual environmnent is activate, checking if the command prompt has the prefix `(venv)`.

To install all the requirements, run the following:

`pip install -r requirements.txt`

This installs, using [pip](https://pypi.python.org/pypi/pip), all the [requirements](#requirements). 

#### Run

After activating *virtualenv*, just type `python3.6 app.py` in the root directory.

### Node.js Express

In the folder `nodejs` there is the WS developed in Node.js. 

The WS has been developed using [Node.js 9.2.0](https://nodejs.org/it/), [Express >4.15](http://flask.pocoo.org/docs/0.12/) as a webdevelopment framework and [Sequelize 4.22](http://docs.sequelizejs.com/) as ORM.

#### Setup

You have to install *Node.js* and [npm](https://www.npmjs.com/) in order to run the project. 

After doing that, just type `npm install` in the project's directory.

#### Run

After installing the requirements, type `npm start` in the project's directory.

## API

Both the WSs have the following endpoints:

- `/hello_world`: a simple HTML page showing greetings;
- `/hello/<user>`: an HTML page showing customized greetings for the user;
- `/fib30`: an HTML page showing the 30th Fibonacci number;
- `/single_user`: an HTML page showing informations about a single user in the database;
- `/all_users`: an HTML page showing informations about all the users;
- `/users_with_cities`: an HTML page showing informations about all the user with their cities;
- `/api/hello_world`: a JSON containing greetings;
- `/api/hello/<user>`: a JSON containing customized greetings for the user;
- `/api/fib30`: a JSON containing the 30th Fibonacci number;
- `/api/single_user`: a JSON containing informations about a single user in the database;
- `/api/all_users`: a JSON containing informations about all the users;
- `/api/users_with_cities`: a JSON containing informations about all the user with their cities;
- `/external/posts`: a JSON containing information about all the posts retrieved from the external source;
- `/external/albums`: a JSON containing information about all the albums retrieved from the external source;
- `/external/photos`: a JSON containing information about all the photos retrieved from the external source;
- `/external/albums_w_photos`: a JSON containing information about all the albums, with the photos it contains, retrieved from the external source;

