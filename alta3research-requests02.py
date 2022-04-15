#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import jsonify
from flask import make_response

app = Flask(__name__)


@app.route("/")
def home_get():
    name = request.cookies.get("name")
    breed = request.cookies.get("breed")
    gender = request.cookies.get("gender")

    application = {'name': name, 'breed': breed, 'gender': gender}

    if name:
        return render_template("application.html", application=application)
    return render_template("form.html")


@app.route("/dog-info")
def dog_info_get():
    dog_info = {
        'breeds': [
            'Pitbull', 'Golden Retriever', 'Pug'
        ],
        'locations': [
            'Fort Collins', 'Denver', 'Boulder'
        ]
    }
    return jsonify(dog_info)


@app.route("/entry", methods=["POST"])
def entry_post():
    data = request.form
    name = data.get('name')
    breed = data.get('dogs')
    gender = "unknown"
    male = data.get('male', None)
    female = data.get('female', None)

    if female:
        gender = 'female'
    elif male:
        gender = 'male'

    application = {'name': name, 'breed': breed, 'gender': gender}

    resp = make_response(redirect(url_for("home_get")))

    for key, value in application.items():
        resp.set_cookie(key, value)

    return resp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2224)
