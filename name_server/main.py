from flask import jsonify
from flask import Flask, session, redirect, url_for, request, render_template, send_file
from flask_cors import CORS
import os
import shutil
import time
import requests

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

FILES = []

STORAGE_IP = ['18.216.86.164', '3.137.205.50', '18.218.51.168']
nodes = len(STORAGE_IP)-1
counter = 0


def chooseNode():
    global counter
    n = counter % nodes
    counter += 1
    return STORAGE_IP[n]

# "refresh", // not related to selected


@app.route('/refresh', methods=['GET'])
def getListDir():
    return jsonify(FILES)


# "copy": from, to
@app.route('/copy', methods=['GET'])
def getCopyFileTo():
    global FILES
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
        if r.status_code == 200:
            FILES = r.json()
    return jsonify(FILES)


# "move": from, to
@app.route('/move', methods=['GET'])
def getMoveFile():
    global FILES
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
        if r.status_code == 200:
            FILES = r.json()
    return jsonify(FILES)


# "mkdir": path
@app.route('/mkdir', methods=['GET'])
def getMkDir():
    global FILES
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
        if r.status_code == 200:
            FILES = r.json()
    return jsonify(FILES)


# "rmdir": path
@app.route('/rmdir', methods=['GET'])
def rmDir():
    global FILES
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
        if r.status_code == 200:
            FILES = r.json()
    return jsonify(FILES)


# "touch": path
@app.route('/touch', methods=['GET'])
def createFile():
    global FILES
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
        if r.status_code == 200:
            FILES = r.json()
    return jsonify(FILES)


# "rm_file": path
@app.route('/rm_file', methods=['GET'])
def rmFile():
    global FILES
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
        if r.status_code == 200:
            FILES = r.json()
    return jsonify(FILES)


# "download", path
@app.route('/download', methods=['GET'])
def download_file():
    global FILES
    storage = chooseNode()
    return jsonify({"url": f'http://{storage}:5000{request.full_path}'})


# "upload", file
@app.route('/upload/', methods=['POST'])
def upload_file():
    global FILES
    print("Filename", [request.form[i] for i in request.form.keys()])
    f = request.files['file']
    f.save(f.filename)
    data = {'file': (f.filename, open(f.filename, 'rb'))}

    for storage in STORAGE_IP:
        r = requests.post(
            f'http://{storage}:5000{request.full_path}', files=data)
        if r.status_code == 200:
            FILES = r.json()
    os.remove(f.filename)
    return jsonify(FILES)


# "rm_rf", // requires confirmation
@app.route('/clear_all', methods=['GET'])
def clear_all():
    global FILES
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
        if r.status_code == 200:
            FILES = r.json()
    return jsonify(FILES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
