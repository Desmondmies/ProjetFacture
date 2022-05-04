import os
from getForm import getForm
from flask import Flask, render_template, request
#render_template permet d'utiliser directement du code HTML
#et de lui passer en paramètre des variables

from Python.Client import Client
from Python.Artisan import Artisan

HTML_DIR = os.path.abspath('./WEB/HTML')
STATIC_DIR = os.path.abspath('./WEB/CSS')

InfoArtisan =   {"surname" : "Matignofle",
  "firstname" : "Robertine",
  "compagny_name" : "salut la compagny",
  "phone" : "00 00 00 00 00",
  "mail_compagny" : "slt_la_comp@gmail.com",
  "adress" : "45 Rue ici",
  "logo" : "path",
  "template_selected" : "STYLE2"
}

app = Flask(__name__, template_folder=HTML_DIR, static_folder=STATIC_DIR)

dico_client = {"surname" : "Matignofle",
  "firstname" : "Robertine",
  "phone" : "00 00 00 00 00",
  "mail" : "slt_la_comp@gmail.com",
  "adress" : "45 Rue ici",
  "description" : "le client "
}


@app.route("/")
def home():
    return render_template("home_page.html")

@app.route("/facture")
def facture():
    return render_template("facture.html")

@app.route("/devis")
def devis():
    return render_template("devis.html")
"""
@app.route("/client")
def client():
    return render_template("client.html", posts = [dico_client]) #posts = variable à passer en paramètre à notre page HTML
"""
@app.route("/client",methods=['POST', 'GET'])
def add_client():
    if request.method == 'POST':
        r = getForm(request.form)
        print(r)
    return render_template("add_client.html", CLIENT = dico_client) #posts = variable à passer en paramètre à notre page HTML

@app.route("/artisan",methods=['POST', 'GET'])
def artisan():
    if request.method == 'POST':
        r = getForm(request.form)
        print(r)
        if "STYLE" in r :
            InfoArtisan["template_selected"] = r
    return render_template("artisan.html",TEMPLATE_ID="Artisan", ARTISAN = InfoArtisan , PATH="/artisan", SEARCH_BAR=True )


if __name__ == "__main__":
    try:
        app.run(debug = True)
    except KeyboardInterrupt:
        print("Application terminé.")

    print(dico_client["surname"])
