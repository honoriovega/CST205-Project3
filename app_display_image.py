# Course: CST 205 
# Title: app_display_image
# Abstract: This file is used to display the images.
# Authors: Honorio Vega, James Barquera
# Date: April 20 2016
# Who worked on which functions: James worked on this file
# Github link: https://github.com/honoriovega/CST205-Project3
# Trello Link : https://trello.com/b/xlsKfNv7/team-256-project-3-cst-205

# import libraries
import os
from uuid import uuid4

from flask import Flask, request, render_template, send_from_directory

__author__ = 'ibininja'

app = Flask(__name__)
# app = Flask(__name__, static_folder="images")



APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    # target = os.path.join(APP_ROOT, 'static/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)

    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("complete.html", image_name=filename)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

# Run the program
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

