from flask import redirect, url_for
from Python.Manager.Artisan import artisan

def home_page_ctrl():
    if artisan.isArtisanComplete():
        return redirect(url_for("formulaire_route"))
    return redirect(url_for("artisan_route"))