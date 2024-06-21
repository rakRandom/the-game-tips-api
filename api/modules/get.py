from api.api import *
from foo import json_get_data

@app.route("/get-author")
@app.route("/get-author/<int:id>")
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
