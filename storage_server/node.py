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


def copyFileTo(source, destination):
    print("COPY FROM", source, "TO", destination)
    shutil.copyfile(source, destination)


def moveFileTo(source, destination):
    print("MOVE FROM", source, "TO", destination)
    shutil.move(source, destination)


def mkdir(path):
    print("NEW DIRECTORY CREATED")
    os.mkdir(path)


def rmdir(path):
    print("REMOVE DIRECTORY")
    shutil.rmtree(path)


def mkfile(path):
    print("NEW FILE CREATED")
    open(path, 'a').close()


def rmfile(path):
    print("REMOVE FILE")
    os.remove(path)


def rm_rf():
    print("REMOVE ALL")
    rmdir(DIR)
    mkdir(DIR)

@app.route('/', methods=['GET'])
def index():
    return "Welcome to DFS!"


# "refresh", // not related to selected
@app.route('/refresh', methods=['GET'])
def getListDir():
    return jsonify(getFiles())


# "copy": from, to
@app.route('/copy', methods=['GET'])
def getCopyFileTo():
    source = DIR + request.args.get('from')[2:]
    destination = DIR + request.args.get('to')[1:]
    copyFileTo(source, destination)
    return jsonify(getFiles())


# "move": from, to
@app.route('/move', methods=['GET'])
def getMoveFile():
    source = DIR + request.args.get('from')[2:]
    destination = DIR + request.args.get('to')[1:]
    moveFileTo(source, destination)
    return jsonify(getFiles())


# "mkdir": path
@app.route('/mkdir', methods=['GET'])
def getMkDir():
    path = DIR + request.args.get('path')
    mkdir(path)
    return jsonify(getFiles())


# "rmdir": path
@app.route('/rmdir', methods=['GET'])
def rmDir():
    path = DIR + request.args.get('path')[2:]
    rmdir(path)
    return jsonify(getFiles())


# "touch": path
@app.route('/touch', methods=['GET'])
def createFile():
    path = DIR + request.args.get('path')
    mkfile(path)
    return jsonify(getFiles())


# "rm_file": path
@app.route('/rm_file', methods=['GET'])
def rmFile():
    path = DIR + request.args.get('path')
    rmfile(path)
    return jsonify(getFiles())


# "download", path
@app.route('/download', methods=['GET'])
def download_file():
    path = DIR + request.args.get('path')[2:]
    return send_file(path, as_attachment=True)


# "upload", file
@app.route('/upload/', methods=['POST'])
def upload_file():
    print("Filename", [request.form[i] for i in request.form.keys()])
    f = request.files['file']
    f.save(DIR + f.filename)
    return jsonify(getFiles())


# "rm_rf", // requires confirmation
@app.route('/clear_all', methods=['GET'])
def clear_all():
    rm_rf()
    return jsonify(getFiles())


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
