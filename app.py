import os
from flask import Flask, send_from_directory

#test scenario
from Python.Manager.Artisan import artisan
from Python.Manager.Client_mng import client_mng
from Python.Manager.Estimate_mng import estimate_mng
from Python.Manager.Invoice_mng import invoice_mng

from Python.Controllers.HomePageCtrl import home_page_ctrl
from Python.Controllers.FormulairePageCtrl import formulaire_page_ctrl
from Python.Controllers.FacturePageCtrl import facture_page_ctrl
from Python.Controllers.DevisPageCtrl import devis_page_ctrl
from Python.Controllers.ClientPageCtrl import client_page_ctrl
from Python.Controllers.ArtisanPageCtrl import artisan_page_ctrl
from Python.Controllers.AddClientPageCtrl import add_client_page_ctrl
from Python.Controllers.AddDevisPageCtrl import add_devis_page_ctrl
from Python.Controllers.AddFacturePageCtrl import add_facture_page_ctrl
from Python.Controllers.ModifyClientPageCtrl import modify_client_page_ctrl
from Python.Controllers.ModifyDevisPageCtrl import modify_devis_page_ctrl
from Python.Controllers.ModifyFacturePageCtrl import modify_facture_page_ctrl

# ---------------------------------------------------------------------------------------------

HTML_DIR = os.path.abspath('./WEB/HTML')
STATIC_DIR = os.path.abspath('./WEB/CSS')

app = Flask(__name__, template_folder=HTML_DIR, static_folder=STATIC_DIR)

# ---------------------------------------------------------------------------------------------

@app.route("/")
def home_route():
    return home_page_ctrl()

@app.route("/formulaire")
def formulaire_route():
    return formulaire_page_ctrl()

@app.route("/facture", methods=[ 'POST', 'GET' ])
def facture_route():
    return facture_page_ctrl()

@app.route("/devis", methods=['POST', 'GET'])
def devis_route():
    return devis_page_ctrl()

@app.route("/client", methods=['POST', 'GET'])
def client_route():
    return client_page_ctrl()

@app.route("/artisan", methods=['POST', 'GET'])
def artisan_route():
    return artisan_page_ctrl()

# ---------------------------------------------------------------------------------------------

@app.route("/add_client", methods=["POST", "GET"])
def add_client_route():
    return add_client_page_ctrl()

@app.route("/add_facture", methods=["POST", "GET"])
def add_facture_route():
    return add_facture_page_ctrl()

@app.route("/add_devis", methods=["POST", "GET"])
def add_devis_route():
    return add_devis_page_ctrl()

# ---------------------------------------------------------------------------------------------

@app.route("/modify_client/<id>", methods=["POST", "GET"])
def modify_client_route(id):
    return modify_client_page_ctrl(int(id))

@app.route("/modify_facture/<id>", methods=["POST", "GET"])
def modify_facture_route(id):
    return modify_facture_page_ctrl(int(id))

@app.route("/modify_devis/<id>", methods=["POST", "GET"])
def modify_devis_route(id):
    return modify_devis_page_ctrl(int(id))

# ---------------------------------------------------------------------------------------------

@app.route("/Images/<path:filename>")
def image_route(filename):
    return send_from_directory(app.root_path + '/Images/', filename)

# ---------------------------------------------------------------------------------------------

def scenario():
    #TEST ARTISAN
    """
    print("\n\n#### ARTISAN #####")
    print(artisan.read_artisan())
    artisan["surname"] = "NOUVEAU NOM"
    print(artisan.read_artisan())
    """

    #TEST CLIENT
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
    #TEST FACTURE
    print("\n\n#### FACTURE #####")
    print("i_ new fact :", invoice_mng.newInvoice_id)
    invoice_mng.create_invoice({"client_id" : 0, "creation_date" : "2022-06-03", "due_date" : "2022-05-30", "comment" : "sdfvsdfvldlkfcrm", "acquitted" : False, "list_items" : ["item1", "item2"]})
    invoice_mng.create_invoice({"client_id" : 0, "creation_date" : "2022-05-03", "due_date" : "2022-05-30", "comment" : "sdfvsdfvldlkfcrm", "acquitted" : False, "list_items" : ["item1", "item2"]})
    print(invoice_mng.read_invoice(0))
    print("id new fact :", invoice_mng.newInvoice_id)
    invoice_mng.update_invoice(0, "surname", "Thomas")
    print(invoice_mng.read_invoice(0))
    invoice_mng.delete_invoice(0)
    print("id new fact :", invoice_mng.newInvoice_id)

    #TEST DEVIS
    """
    print("\n\n#### DEVIS #####")
    print("i_ new estimate :", estimate_mng.newEstimate_id)
    estimate_mng.create_estimate({"client_id" : 0, "creation_date" : "03/05/2022", "due_date" : "30/05/2022", "comment" : "sdfvsdfvldlkfcrm", "acquitted" : False, "list_items" : ["item1", "item2"]})
    print(estimate_mng.read_estimate(0))
    print("id new estimate :", estimate_mng.newEstimate_id)
    estimate_mng.update_estimate(0, "surname", "Thomas")
    print(estimate_mng.read_estimate(0))
    estimate_mng.delete_estimate(0)
    print("id new estimate :", estimate_mng.newEstimate_id)
    """

# ---------------------------------------------------------------------------------------------

if __name__ == "__main__":
    #scenario()
    try:
        app.run(debug = True)
    except KeyboardInterrupt:
        print("Application terminé.")
