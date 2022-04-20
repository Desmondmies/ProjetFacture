import os
from flask import Flask, render_template
#render_template permet d'utiliser directement du code HTML
#et de lui passer en paramètre des variables

HTML_DIR = os.path.abspath('./WEB/HTML')
STATIC_DIR = os.path.abspath('./WEB/CSS')

app = Flask(__name__, template_folder=HTML_DIR, static_folder=STATIC_DIR)

dico_client = {"Nom" : "noooom...",
                "Prenom" : "...bril",
                "Tel" : "06 06 06 06 06",
                "Mail" : "machin@qqchmail.fr",
                "Description" : "Riche client qui vient souvent etc..........."}

@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/formulaire")
def formulaire():
    return render_template("formulaire.html")

@app.route("/facture")
def facture():
    return render_template("facture.html")

@app.route("/devis")
def devis():
    return render_template("devis.html")

@app.route("/client")
def client():
    return render_template("client.html", posts = [dico_client]) #posts = variable à passer en paramètre à notre page HTML

@app.route("/artisan")
def artisan():
    return render_template("artisan.html")


if __name__ == "__main__":
    print("test github/atom")
    try:
        app.run(debug = True)
    except KeyboardInterrupt:
        print("Application terminé.")
