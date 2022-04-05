#!/usr/bin/python
# -*- coding: Utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__,template_folder='/home/etudiants/rbenamir142/Bureau/projet_UML/facture-main/Template', static_folder='/home/etudiants/rbenamir142/Bureau/projet_UML/facture-main/Template')

@app.route("/")

def home():
    return render_template("./form.html")

if __name__ == '__main__':
    app.run(debug=True)
