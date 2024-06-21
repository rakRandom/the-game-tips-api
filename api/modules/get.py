from api.api import *

@app.route("/get-author/<int:id>", methods=['GET'])
@cross_origin()
def get_author(id):
    file_content: dict
    
    with open("api/data/authors/data.json", "r", encoding="UTF-8") as file:
        file_content = load(file)
    
    content = file_content[id]

    if not content:
        return jsonify("{}", 200)

    response = app.response_class(
        response=dumps(content),
        status=200,
        mimetype='application/json'
    )

    return response
