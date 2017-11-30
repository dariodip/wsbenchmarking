from flask import Flask
from routes.api import api_routes
from routes.pages import pages_routes
from routes.externals import ext_routes
from data import db


app = Flask(__name__, static_url_path='/static')
db_source = db.db_source
app.register_blueprint(api_routes)
app.register_blueprint(pages_routes)
app.register_blueprint(ext_routes)


if __name__ == '__main__':
    app.run(port=3000)
