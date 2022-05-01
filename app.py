import os
from flask import Flask, render_template #render_template permet d'utiliser directement du code HTML et de lui passer en paramètre des variables

from Python.Manager.Artisan import Artisan
from Python.Manager.Client_mng import Client_mng

from Python.Client import Client
from Python.Invoice import Invoice


HTML_DIR = os.path.abspath('./WEB/HTML')
STATIC_DIR = os.path.abspath('./WEB/CSS')

app = Flask(__name__, template_folder=HTML_DIR, static_folder=STATIC_DIR)

@app.route("/")
def home():
    return render_template("home_page.html")

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

def initialisation():
    artisan = Artisan() #On charge les données de l'artisan
    client_mng = Client_mng()
    
    client_mng.create_client({"firstname" : "proc", "surname" : "thom", "phone" : "00 00 00 00 00", "mail" : "sdfvsdfv@ldlkf.com", "adress" : "chemin des petits poids", "postcode" : 83300, "description" : "cooooommmmm"})
    print(client_mng.read_client(0))
    client_mng.update_client(0, "surname", "Thomas")
    print(client_mng.read_client(0))
    client_mng.delete_client(0)
    #On charge les données des factures
    #On charge les données des devis
    
if __name__ == "__main__":
    initialisation()
    """
    try:
        app.run(debug = True)
    except KeyboardInterrupt:
        print("Application terminé.")
    """
