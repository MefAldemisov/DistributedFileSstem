from flask import jsonify
from flask import Flask, session, redirect, url_for, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

files = [
    {
        "index": 0,
        "name": "dist",
        "size": "0",
        "upd": "23.05.20",
        "data": [],
    },
    {
        "index": 1,
        "name": "dir",
        "size": "1024",
        "data": [
            {
                "index": 0,
                "name": "helloworld.c",
                "size": "256",
                "upd": "23.05.19",
            },
            {
                "index": 1,
                "name": "helloworld.cpp",
                "size": "184",
                "upd": "23.05.20",
            },
        ],
    },
    {
        "index": 2,
        "name": "helloworld.c",
        "size": "256",
        "upd": "23.05.19",
    },
    {
        "index": 3,
        "name": "helloworld.cpp",
        "size": "184",
        "upd": "23.05.20",
    },
    {
        "index": 4,
        "name": "aaa.txt",
        "size": "256",
        "upd": "23.05.19",
    },
],


def getFiles():
    return files


def copyFileTo(soutce, destination):
    print("Copy from", soutce, "to", destination)


def moveFileTo(soutce, destination):
    print("Move from", soutce, "to", destination)


def mkdir(path):
    print("MKDIR")


# "refresh", // not related to selected
@app.route('/refresh', methods=['GET'])
def getListDir():
    return jsonify(getFiles())


# "copy": from, to
@app.route('/copy', methods=['GET'])
def getCopyFileTo():
    source = request.args.get('from')
    destination = request.args.get('to')
    copyFileTo(source, destination)
    return jsonify(getFiles())


# "move": from, to
@app.route('/move', methods=['GET'])
def getMoveFile():
    source = request.args.get('from')
    destination = request.args.get('to')
    moveFileTo(source, destination)
    return jsonify(getFiles())


# "mkdir": path
@app.route('/mkdir', methods=['GET'])
def getMkDir():
    path = request.args.get('path')
    mkdir(path)
    return jsonify(getFiles())



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
