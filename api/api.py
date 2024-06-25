from flask import Flask
from flask import send_from_directory
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from json import dumps, load
from api.modules.get import json_get_data

app = Flask(__name__)
app.debug = True
CORS(app)

# from database import db
# from database import models

@app.route("/get-user/<user_id>", methods=['GET'])
@cross_origin()
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    response = app.response_class(
        response=dumps(user_data),
        status=200,
        mimetype='application/json'
    )

    return response

@app.route("/get-index/<int:id>", methods=['GET'])
@cross_origin()
def get_index(id):
    try:
        content = json_get_data("landing_page/data.json")[id]
    except:
        return jsonify("{}", 200)

    response = app.response_class(
        response=dumps(content),
        status=200,
        mimetype='application/json'
    )

    return response

@app.route("/get-author", methods=['GET'])
@app.route("/get-author/<int:id>", methods=['GET'])
@cross_origin()
def get_author(id=None):
    content = json_get_data("authors/data.json")

    if not content:
        return jsonify("{}", 200)
    
    try:
        if id:
            content = content[id]
    except:
        return jsonify("{}", 200)

    if not content:
        return jsonify("{}", 200)

    response = app.response_class(
        response=dumps(content),
        status=200,
        mimetype='application/json'
    )

    return response

@app.route("/<path:filename>", methods=['GET'])
def get_image(filename):
    return send_from_directory("", filename, mimetype="image", as_attachment=False)

@app.route("/json/<path:filename>", methods=['GET', 'POST'])
@cross_origin()
def json(filename):
    if request.method == 'GET':
        return send_from_directory("", filename, mimetype="application/json", as_attachment=False)
    elif request.method == 'POST':
        data = request.get_json()
        if "content" not in data.keys():
            return {}, 204
        with open(filename, "w", encoding="UTF-8") as file:
            file.write(data["content"])
            return {}, 200
