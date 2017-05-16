# Course: CST 205 
# Title: app_display_multiple_images.py
# Abstract: This file would display multiple images the user has uploaded
#           The user would then be presented with a menu of options such as
#           apply median filter, etc.
# Authors: Honorio Vega, James Barquera
# Date: April 20 2016
# Who worked on which functions: Honorio Worked on this file
# Github link: https://github.com/honoriovega/CST205-Project3
# Trello Link : https://trello.com/b/xlsKfNv7/team-256-project-3-cst-205

import os


from flask import Flask, request, render_template, send_from_directory

__author__ = 'ibininja'

app = Flask(__name__)



APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
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

@app.route('/gallery')
def get_gallery():
    image_names = os.listdir('./images')
    print(image_names)
    return render_template("gallery.html", image_names=image_names)

if __name__ == "__main__":
    app.run(port=4555, debug=True)