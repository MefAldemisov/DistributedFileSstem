from flask import jsonify
from flask import Flask, session, redirect, url_for, request, render_template, send_file
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
        "name": "main.py",
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


def rmdir(path):
    print("RMDIR")


def mkfile(path):
    print("NEW FILE")


def rmfile(path):
    print("RM FILE")


def rm_rf():
    # clear all
    global files
    files = []


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


# "rmdir": path
@app.route('/rmdir', methods=['GET'])
def rmDir():
    path = request.args.get('path')
    rmdir(path)
    return jsonify(getFiles())


# "touch": path
@app.route('/touch', methods=['GET'])
def createFile():
    path = request.args.get('path')
    mkfile(path)
    return jsonify(getFiles())


# "rm_file": path
@app.route('/rm_file', methods=['GET'])
def rmFile():
    path = request.args.get('path')
    rmfile(path)
    return jsonify(getFiles())


# "download", path
@app.route('/download', methods=['GET'])
def download_file():
    path = request.args.get('path')
    return send_file(path, as_attachment=True)


# "upload", file
@app.route('/upload/', methods=['POST'])
def upload_file():
    print("Filename", [request.form[i] for i in request.form.keys()])
    f = request.files['file']
    f.save(f.filename)
    return jsonify(getFiles())


# "rm_rf", // requires confirmation
@app.route('/clear_all', methods=['GET'])
def clear_all():
    rm_rf()
    return jsonify(getFiles())


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
