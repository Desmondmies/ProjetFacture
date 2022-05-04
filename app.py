import os
from flask import Flask, render_template, request
#render_template permet d'utiliser directement du code HTML
#et de lui passer en paramètre des variables

from Python.Client import Client
from Python.Invoice import Invoice

from Python.Manager.Artisan import Artisan
from Python.Manager.Client_mng import Client_mng

from Python.FormRequestHandlers.FactureFormRequest import getfactureForm
from Python.FormRequestHandlers.DevisFormRequest import getdevisForm
from Python.FormRequestHandlers.ClientFormRequest import getclientForm
from Python.FormRequestHandlers.ArtisanFormRequest import getartisanForm

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

#ARTISAN = Artisan("ENTREPRISE","Saidi", "Fouad", "06 06 06 06 06", "entreprise@mail.com","23 adresse Toulon")

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
			filter_btn_toggle = not filter_btn_toggle
		elif "Filter_" in r:
			filter_idx = get_new_search_filter_index(r)
			Client_mng.change_search_filter(filter_idx)

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
	#global ARTISAN
	if request.method == 'POST':
		r = getartisanForm(request.form)
		print(r)
		if "STYLE" in r :
			print("style changed")
			#ARTISAN.style_prefere = r
	return render_template("artisan.html",
							TEMPLATE_ID="Artisan",
							#STYLE_ID = ARTISAN.style_prefere,
							PATH="/artisan",
							SEARCH_BAR=False
							#NOM_ENTREPRISE=ARTISAN.nom_ent,
							#NOM = ARTISAN.nom,
							#PRENOM = ARTISAN.prenom,
							#TEL=ARTISAN.tel,
							#MAIL=ARTISAN.mail_comp,
							#ADRESSE=ARTISAN.adresse_ent
							)

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

# ---------------------------------------------------------------------------------------------

if __name__ == "__main__":
    initialisation()
    try:
        app.run(debug = True)
    except KeyboardInterrupt:
        print("Application terminé.")
