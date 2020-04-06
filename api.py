from flask import Flask, jsonify, json, request

pl = [
    {
        "Name": "Orad Exsol",
        "Age": "19",
        "Job": "horse farm"
    },
    {
        "Name": "moshe Exsol",
        "Age": "56",
        "Job": "haifaport"
    },
    {
        "Name": "Dalit Exsol",
        "Age": "52",
        "Job": "CEO digital-cut/lrps"
    }
]

api = Flask(__name__)



@api.route('/func', methods=['GET'])
def get():
    a = jsonify(pl)
    return a


@api.route('/isalive', methods=['GET'])
def isalive():
    return "true"


@api.route('/func', methods=['PUT'])
def put():
    body = request.json
    pl.insert(0, body)
    a = jsonify(pl)
    return a


@api.route('/func', methods=['DELETE'])
def delete():
    body = request.json
    for i in range(0, len(pl)-1):
        b = pl[i]
        if body["song"] == b["song"]:
            pl.remove(pl[i])
    a = jsonify(pl)
    return a


if __name__ == "__main__":
    api.run(debug=True, port=80, host="0.0.0.0")
