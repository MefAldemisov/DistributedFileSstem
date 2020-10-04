from flask import jsonify
from flask import Flask, session, redirect, url_for, request, render_template, send_file
from flask_cors import CORS
import os
import shutil
import time
import requests

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
DIR = "./fs/"
try:
    os.mkdir(DIR)
except:
    print("Fs already exist")

STORAGE_IP = ['172.17.0.2']
nodes = len(STORAGE_IP)
counter = 0

def chooseNode():
    n = counter % nodes
    counter+=1
    return STORAGE_IP[n]


def getFiles(dir=DIR):
    ls_dir = os.listdir(dir)
    data = [{"index": i,
             "name": ls_dir[i],
             "size": os.stat(dir+ls_dir[i]).st_size,
             "upd": time.ctime(os.stat(dir+ls_dir[i]).st_mtime)} for i in range(len(ls_dir))]
    for d in data:
        print(dir + d['name'])
        if os.path.isdir(dir + d['name']):
            print("YES", dir + d['name'])
            d['data'] = getFiles(dir + d['name'] + "/")
    return data


# "refresh", // not related to selected
@app.route('/refresh', methods=['GET'])
def getListDir():
    return jsonify(getFiles())


# "copy": from, to
@app.route('/copy', methods=['GET'])
def getCopyFileTo():
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
    #return jsonify(getFiles())
    return r


# "move": from, to
@app.route('/move', methods=['GET'])
def getMoveFile():
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
    #return jsonify(getFiles())
    return r


# "mkdir": path
@app.route('/mkdir', methods=['GET'])
def getMkDir():
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
    #return jsonify(getFiles())
    return r


# "rmdir": path
@app.route('/rmdir', methods=['GET'])
def rmDir():
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
    #return jsonify(getFiles())
    return r


# "touch": path
@app.route('/touch', methods=['GET'])
def createFile():
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}')
    #return jsonify(getFiles())
    return r


# "rm_file": path
@app.route('/rm_file', methods=['GET'])
def rmFile():
    for storage in STORAGE_IP:
        r = requests.get(f'http://{storage}:5000{request.full_path}') 
    #return jsonify(getFiles())
    return r


# "download", path
@app.route('/download', methods=['GET'])
def download_file():
    storage = chooseNode()
    r = requests.get(f'http://{storage}:5000{request.full_path}')
    return send_file(r, as_attachment=True)


# "upload", file
@app.route('/upload/', methods=['POST'])
def upload_file():
    print("Filename", [request.form[i] for i in request.form.keys()])
    for storage in STORAGE_IP:
        r = requests.post(f'http://{storage}:5000{request.full_path}')
    #return jsonify(getFiles())
    return r


# "rm_rf", // requires confirmation
@app.route('/clear_all', methods=['GET'])
def clear_all():
    for storage in STORAGE_IP:
        r = requests.post(f'http://{storage}:5000{request.full_path}')
    #return jsonify(getFiles())
    return r


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
