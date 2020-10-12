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
DOWN_NODES = []

STORAGE_IP = ['18.217.14.176', '3.129.83.36', '3.138.70.26']
BACKUP_NODE = '3.138.70.26'
counter = 0


def chooseNode():
    upCheck()
    global counter
    nodes = len(STORAGE_IP)
    n = counter % nodes
    counter += 1
    if STORAGE_IP[n] != BACKUP_NODE:
        return STORAGE_IP[n]
    n = counter % nodes
    counter += 1
    return STORAGE_IP[n]

# "refresh", // not related to selected


@app.route('/refresh', methods=['GET'])
def getListDir():
    # upCheck()
    return jsonify(FILES)


# "copy": from, to
@app.route('/copy', methods=['GET'])
def getCopyFileTo():
    upCheck()
    global FILES
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
        if r.status_code == 200:
            FILES = r.json()
    return jsonify(FILES)


# "move": from, to
@app.route('/move', methods=['GET'])
def getMoveFile():
    upCheck()
    global FILES
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
        if r.status_code == 200:
            FILES = r.json()
    return jsonify(FILES)


# "mkdir": path
@app.route('/mkdir', methods=['GET'])
def getMkDir():
    upCheck()
    global FILES
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
        if r.status_code == 200:
            FILES = r.json()
    return jsonify(FILES)


# "rmdir": path
@app.route('/rmdir', methods=['GET'])
def rmDir():
    upCheck()
    global FILES
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
        if r.status_code == 200:
            FILES = r.json()
    return jsonify(FILES)


# "touch": path
@app.route('/touch', methods=['GET'])
def createFile():
    upCheck()
    global FILES
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
        if r.status_code == 200:
            FILES = r.json()
    return jsonify(FILES)


# "rm_file": path
@app.route('/rm_file', methods=['GET'])
def rmFile():
    upCheck()
    global FILES
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
        if r.status_code == 200:
            FILES = r.json()
    return jsonify(FILES)


def getFiles(node, path):
    paths = []
    files = []
    if 'data' in node:
        paths.append(path + node['name'])
        for n in node['data']:
            tmp = getFiles(n, path + node['name'] + "/")
            files.extend(tmp[1])
            paths.extend(tmp[0])
    else:
        files.append(path + node['name'])
    return paths, files


def upCheck():
    for node in STORAGE_IP:
        try:
            res = requests.get(f'http://{node}:5000/ping', timeout=3)
        except requests.exceptions.ConnectionError:
            STORAGE_IP.remove(node)
            DOWN_NODES.append(node)
            return 500
        else:
            if res.status_code != 200:
                STORAGE_IP.remove(node)
                DOWN_NODES.append(node)
    for node in DOWN_NODES:
        try:
            res = requests.get(f'http://{node}:5000/ping', timeout=3)
        except requests.exceptions.ConnectionError:
            pass
        else:
            if res.status_code == 200:
                DOWN_NODES.remove(node)
                files = []
                paths = []
                for n in FILES:
                    tmp = getFiles(n, "")
                    files.extend(tmp[1])
                    paths.extend(tmp[0])
                d = {'dirs': paths, 'files': files, 'ip': BACKUP_NODE}
                res = requests.post(
                    f'http://{node}:5000/recovery', data=d)
                STORAGE_IP.append(node)

# "download", path


@app.route('/download', methods=['GET'])
def download_file():
    upCheck()
    global FILES
    storage = chooseNode()
    return jsonify({"url": f'http://{storage}:5000{request.full_path}'})


# "upload", file
@app.route('/upload/', methods=['POST'])
def upload_file():
    upCheck()
    global FILES

    path = request.form["path"]
    dirs = "."
    if("/" in path):
        dirs = "/".join(path.split("/")[:-1])  # don't add filename to the path

    print("Path", dirs)
    f = request.files['file']
    f.save(f.filename)
    data = {'file': (f.filename, open(f.filename, 'rb'))}

    for storage in STORAGE_IP:
        r = requests.post(
            f'http://{storage}:5000{request.full_path}', files=data, data={"path": dirs})
        if r.status_code == 200:
            FILES = r.json()
    os.remove(f.filename)
    return jsonify(FILES)


# "rm_rf", // requires confirmation
@app.route('/clear_all', methods=['GET'])
def clear_all():
    upCheck()
    global FILES
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
        if r.status_code == 200:
            FILES = r.json()
    return jsonify(FILES)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
