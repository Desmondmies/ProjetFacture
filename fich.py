#!/usr/bin/python
# -*- coding: Utf-8 -*-

from flask import Flask, render_template
import os

TEMPLATE_DIR = os.path.abspath('./Template')
STATIC_DIR = os.path.abspath('./Template')

app = Flask(__name__,template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route("/")

def home():
    return render_template("./form.html")

if __name__ == '__main__':
    app.run(debug=True)
