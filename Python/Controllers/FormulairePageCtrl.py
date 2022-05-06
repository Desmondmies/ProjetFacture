from re import TEMPLATE
from flask import render_template

def formulaire_page_ctrl():
    return render_template("formulaire.html")