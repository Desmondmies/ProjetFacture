import os
from flask import Flask, render_template #render_template permet d'utiliser directement du code HTML et de lui passer en paramètre des variables

from Python.Manager.Artisan import Artisan
from Python.Manager.Client_mng import Client_mng
from Python.Manager.Invoice_mng import Invoice_mng

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

def initialisation() -> None:
    artisan = Artisan() #On charge les données de l'artisan
    client_mng = Client_mng()
    invoice_mng = Invoice_mng()
    scenario(artisan, client_mng, invoice_mng)
    
    #On charge les données des factures
    #On charge les données des devis
    return

def scenario(artisan, client_mng, invoice_mng):
    """
    TEST ARTISAN
    """
    print("\n\n#### ARTISAN #####")
    print(artisan.read_artisan())
    artisan["surname"] = "NOUVEAU NOM"
    print(artisan.read_artisan())

    """
    TEST CLIENT
    """
    print("\n\n#### CLIENT #####")
    print("id new client :", client_mng.newClient_id)
    client_mng.create_client({"firstname" : "proc", "surname" : "thom", "phone" : "00 00 00 00 00", "mail" : "sdfvsdfv@ldlkf.com", "adress" : "chemin des petits poids", "postcode" : 83300, "description" : "cooooommmmm"})
    print(client_mng.read_client(0))
    print("id new client :", client_mng.newClient_id)
    client_mng.update_client(0, "surname", "Thomas")
    print(client_mng.read_client(0))
    client_mng.delete_client(0)
    print("id new client :", client_mng.newClient_id)

    """
    TEST FACTURE
    """
    print("\n\n#### FACTURE #####")
    print("i_ new fact :", invoice_mng.newInvoice_id)
    invoice_mng.create_invoice({"client_id" : 0, "creation_date" : "03/05/2022", "due_date" : "30/05/2022", "comment" : "sdfvsdfvldlkfcrm", "acquitted" : False, "list_items" : ["item1", "item2"]})
    print(invoice_mng.read_invoice(0))
    print("id new fact :", invoice_mng.newInvoice_id)
    invoice_mng.update_invoice(0, "surname", "Thomas")
    print(invoice_mng.read_invoice(0))
    invoice_mng.delete_invoice(0)
    print("id new fact :", invoice_mng.newInvoice_id)
    

if __name__ == "__main__":
    initialisation()
    """
    try:
        app.run(debug = True)
    except KeyboardInterrupt:
        print("Application terminé.")
    """
