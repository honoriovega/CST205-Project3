import os
from flask import Flask, render_template, request
# Course: CST 205 
# Title: app_basic.py
# Abstract: An implementation that is used to upload files
# Authors: Honorio Vega, James Barquera
# Date: April 20 2016
# Who worked on which functions:  James Barquera worked on this file
# Github link: https://github.com/honoriovega/CST205-Project3

__author__ = 'ibininja'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template("complete.html")

if __name__ == "__main__":
    app.run(port=4555, debug=True)