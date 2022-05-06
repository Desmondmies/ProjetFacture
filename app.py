import os
from flask import Flask, redirect, render_template, request, url_for
#render_template permet d'utiliser directement du code HTML
#et de lui passer en paramètre des variables

from Python.Manager.Artisan import artisan as instance_artisan
from Python.Manager.Client_mng import client_mng as instance_client_mng
from Python.Manager.Invoice_mng import invoice_mng as instance_invoice_mng
from Python.Manager.Estimate_mng import estimate_mng as instance_estimate_mng

from Python.FormRequestHandlers.FactureFormRequest import getfactureForm
from Python.FormRequestHandlers.DevisFormRequest import getdevisForm
from Python.FormRequestHandlers.ClientFormRequest import getclientForm
from Python.FormRequestHandlers.ArtisanFormRequest import getartisanForm
from Python.FormRequestHandlers.Add_CardFormRequest import getcardForm

# ---------------------------------------------------------------------------------------------

HTML_DIR = os.path.abspath('./WEB/HTML')
STATIC_DIR = os.path.abspath('./WEB/CSS')

app = Flask(__name__, template_folder=HTML_DIR, static_folder=STATIC_DIR)

# ---------------------------------------------------------------------------------------------

client1 = {"Nom" : "noooom...",
            "Prenom" : "...bril",
            "Tel" : "06 06 06 06 06",
            "Mail" : "machin@qqchmail.fr",
            "Adresse": "82, rue des sapins",
            "Description" : "Riche client qui vient souvent etc..........."}
client2 = {"Nom" : "Loru",
            "Prenom" : "Jean",
            "Tel" : "06 21 54 12 36",
            "Mail" : "machin@qqchmail.fr",
            "Adresse": "82, sapins"} #si le champs description n'existe pas, apparement tout se passe bien, aucune erreur
Clients = [client1, client2]

InfoArtisan =   {"surname" : "Matignofle",
  "firstname" : "Robertine",
  "compagny_name" : "salut la compagny",
  "phone" : "00 00 00 00 00",
  "mail_compagny" : "slt_la_comp@gmail.com",
  "adress" : "45 Rue ici",
  "logo" : "path",
  "template_selected" : "STYLE2"
}

filter_btn_toggle = False
search_filter_index = 0

# ---------------------------------------------------------------------------------------------

@app.route("/")
def home():
    return artisan()

@app.route("/formulaire")
def formulaire():
    return render_template("formulaire.html")

@app.route("/facture", methods=[ 'POST', 'GET' ])
def facture():
    global filter_btn_toggle

    if request.method == 'POST':
        r = getfactureForm(request.form)
        print(r)
        if r == "FILTER":
            filter_btn_toggle = not filter_btn_toggle
        elif "Filter_" in r:
            get_new_search_filter_index(r)
        elif r == "ADD":
            #clic sur le bouton add
            return redirect(url_for("add_facture"))

    #return à la bonne page en fonction du btn bandeau == "Voir Client" ou autre
    return render_template("facture.html",
                            TEMPLATE_ID="Facture",
                            PATH="/facture",
                            SEARCH_BAR=True,
                            FILTER_TOGGLE= filter_btn_toggle,
                            SEARCH_IDX=search_filter_index)

@app.route("/devis", methods=['POST', 'GET'])
def devis():
    global filter_btn_toggle

    if request.method == 'POST':
        r = getdevisForm(request.form)
        print(r)
        if r == "FILTER":
            filter_btn_toggle = not filter_btn_toggle
        elif "Filter_" in r:
            get_new_search_filter_index(r)
        elif r == "ADD":
            #clic sur le bouton add
            return redirect(url_for("add_devis"))

    return render_template("devis.html",
                            TEMPLATE_ID="Devis",
                            PATH="/devis",
                            SEARCH_BAR=True,
                            FILTER_TOGGLE = filter_btn_toggle,
                            SEARCH_IDX = search_filter_index)

@app.route("/client", methods=['POST', 'GET'])
def client():
    global filter_btn_toggle

    if request.method == 'POST':
        r = getclientForm(request.form)
        print(r)
        if r == "FILTER":
            # clic sur le bouton filtre de la barre de recherche
            filter_btn_toggle = not filter_btn_toggle
        elif "Filter_" in r:
            # changement du filtre de la barre de recherche
            filter_idx = get_new_search_filter_index(r)
            Client_mng.change_search_filter(filter_idx)
        elif r == "ADD":
            #clic sur le bouton add
            return redirect(url_for("add_client"))

    #posts = variable à passer en paramètre à notre page HTML
    return render_template("client.html",
                            CLIENTS_DATA = Clients,
                            TEMPLATE_ID="Client",
                            PATH="/client",
                            SEARCH_BAR=True,
                            FILTER_TOGGLE = filter_btn_toggle,
                            SEARCH_IDX = search_filter_index)

@app.route("/artisan", methods=['POST', 'GET'])
def artisan():
    global InfoArtisan

    if request.method == 'POST':
        r = getartisanForm(request.form)
        print(r)
        if "STYLE" in r :
            print("style changed")
            InfoArtisan["template_selected"] = r
    return render_template("artisan.html",
                            TEMPLATE_ID="Artisan",
                            ARTISAN= InfoArtisan,
                            PATH="/artisan",
                            SEARCH_BAR=False )

# ---------------------------------------------------------------------------------------------

@app.route("/add_client", methods=["POST", "GET"])
def add_client():
    if request.method == 'POST':
        r = getcardForm(request.form)
        print(r)
    return render_template("add_client.html",
                            PATH = "/add_client")

@app.route("/add_facture", methods=["POST", "GET"])
def add_facture():
    if request.method == 'POST':
        r = getcardForm(request.form)
        print(r)
    return render_template("add_facture.html",
                            PATH = "/add_facture")

@app.route("/add_devis", methods=["POST", "GET"])
def add_devis():
    if request.method == 'POST':
        r = getcardForm(request.form)
        print(r)
    return render_template("add_devis.html",
                            PATH = "/add_devis")

# ---------------------------------------------------------------------------------------------

def get_new_search_filter_index(r):
	global search_filter_index

	if r == "Filter_Name":
		search_filter_index = 0
	elif r == "Filter_Address":
		search_filter_index = 1
	elif r == "Filter_Tel":
		search_filter_index = 2
	return search_filter_index

def scenario():
    #TEST ARTISAN
    """
    print("\n\n#### ARTISAN #####")
    print(instance_artisan.read_artisan())
    instance_artisan["surname"] = "test nom"
    print(instance_artisan.read_artisan())
    """
    
    #TEST CLIENT
    """
    print("\n\n#### CLIENT #####")
    print("id new client :", instance_client_mng.newClient_id)
    instance_client_mng.create_client({"firstname" : "proc", "surname" : "thom", "phone" : "00 00 00 00 00", "mail" : "sdfvsdfv@ldlkf.com", "adress" : "chemin des petits poids", "postcode" : 83300, "description" : "cooooommmmm"})
    print(instance_client_mng.read_client(0))
    print("id new client :", instance_client_mng.newClient_id)
    instance_client_mng.update_client(0, "surname", "Thomas")
    print(instance_client_mng.read_client(0))
    #instance_client_mng.delete_client(0)
    #print("id new client :", instance_client_mng.newClient_id)
    """

    #TEST FACTURE
    print("\n\n#### FACTURE #####")
    print("id new fact :", instance_invoice_mng.newInvoice_id)
    instance_invoice_mng.create_invoice({"client_id" : 0, "creation_date" : "2022-06-03", "due_date" : "2022-05-30", "comment" : "sdfvsdfvldlkfcrm", "acquitted" : False, "list_items" : [{"name" : "nom", "description" : "description du produit", "quantity":"12 en h ou unité", "price" : 100}]})
    instance_invoice_mng.create_invoice({"client_id" : 0, "creation_date" : "2022-05-03", "due_date" : "2022-05-30", "comment" : "sdfvsdfvldlkfcrm", "acquitted" : False, "list_items" : ["item1"], "list_deposits" : [{"amount" : 2222, "payment_date" : "2022-20-06"}]})
    print(instance_invoice_mng.read_invoice(0))
    print(instance_invoice_mng.read_invoice(1))
    print("id new fact :", instance_invoice_mng.newInvoice_id)
    instance_invoice_mng.create_item(0, {"name" : "ITEM2222222"})
    #instance_invoice_mng.update_invoice(0, "comment", "Nouveau commentaire")
    #print(instance_invoice_mng.read_invoice(0))
    #instance_invoice_mng.update_item(0, 1, "name", "COUCOOOUUUUU")
    print(instance_invoice_mng.read_invoice(0))
    instance_invoice_mng.create_deposit(1, {"amount" : 1111, "payment_date" : "2022-06-03"})
    print(instance_invoice_mng.read_invoice(1))
    #instance_invoice_mng.delete_item(0, 1)
    #print(instance_invoice_mng.read_invoice(0))
    #instance_invoice_mng.delete_invoice(0)
    #print("id new fact :", instance_invoice_mng.newInvoice_id)

    #TEST DEVIS
    """
    print("\n\n#### DEVIS #####")
    print("i_ new estimate :", instance_estimate_mng.newEstimate_id)
    instance_estimate_mng.create_estimate({"client_id" : 0, "creation_date" : "03/05/2022", "comment" : "sdfvsdfvldlkfcrm", "list_items" : ["item1", "item2"]})
    print(instance_estimate_mng.read_estimate(0))
    print("id new estimate :", instance_estimate_mng.newEstimate_id)
    instance_estimate_mng.update_estimate(0, "comment", "cooooooommmmm 222222222")
    print(instance_estimate_mng.read_estimate(0))
    #instance_estimate_mng.delete_estimate(0)
    #print("id new estimate :", instance_estimate_mng.newEstimate_id)
    """

# ---------------------------------------------------------------------------------------------

if __name__ == "__main__":
    scenario()
    """
    try:
        app.run(debug = True)
    except KeyboardInterrupt:
        print("Application terminé.")
    """