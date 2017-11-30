from flask import Blueprint, jsonify
import requests
import json


external_resource_URL = "https://jsonplaceholder.typicode.com"
ext_routes = Blueprint('external', __name__)


@ext_routes.route('/external/posts', methods=['GET'])
def all_posts():
    r = requests.get("http://jsonplaceholder.typicode.com/posts")
    return jsonify(json.loads(r.text))


@ext_routes.route('/external/albums', methods=['GET'])
def all_albums():
    r = requests.get("http://jsonplaceholder.typicode.com/albums")
    return jsonify(json.loads(r.text))


@ext_routes.route('/external/photos', methods=['GET'])
def all_photos():
    r = requests.get("http://jsonplaceholder.typicode.com/photos")
    return jsonify(json.loads(r.text))


@ext_routes.route('/external/albums_w_photos', methods=['GET'])
def album_w_photos():
    ra = requests.get("http://jsonplaceholder.typicode.com/albums")
    rp = requests.get("http://jsonplaceholder.typicode.com/photos")
    album_list = json.loads(ra.text)
    photo_list = json.loads(rp.text)
    for album in album_list:
        album['photos'] = [ph for ph in photo_list if ph['albumId'] == album['id']]
    return jsonify(album_list)
