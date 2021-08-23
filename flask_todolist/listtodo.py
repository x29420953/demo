#listtodo.py

from model import List
from flask.json import jsonify
from flask import Blueprint, request, render_template, url_for
from app import db
import datetime

app_api = Blueprint('api', __name__, template_folder="templates")

api = [{
    "content": "這是第一個備忘錄",
    "created_at": "Mon, 12 Apr 2021 21:41:31 GMT",
    "id": 3
}, {
    "content": "這是第二個備忘錄",
    "created_at": "Fri, 30 Jul 2021 04:14:51 GMT",
    "id": 27
}, {
    "content": "這是第三個備忘錄",
    "created_at": "Fri, 30 Jul 2021 04:15:43 GMT",
    "id": 28
}]


@app_api.route('/todo')
def get_all():

    return render_template("index.html", temp=api)


@app_api.route('/todo/<id>')
def get_one(id):

    for i in api:
        if i['id'] == int(id):
            return i
