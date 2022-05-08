from flask import render_template, request

from Python.FormRequestHandlers.FormulaireFormRequest import getformulaireForm

from Python.Manager.Artisan import artisan
from Python.Manager.Invoice_mng import invoice_mng
from Python.Manager.Estimate_mng import estimate_mng
from Python.Manager.Client_mng import client_mng

from Python.Utils.SumItemsDeposits import get_total_price, get_total_deposits

def formulaire_page_ctrl(factureId = None, devisId = None):

    facture, devis, client = None, None, None
    total = None
    restant = None
    no_header = None

    path = "/formulaire"

    clients = client_mng.dict_clients

    if factureId != None:
        facture = invoice_mng.read_invoice(factureId)
        client = client_mng.read_client(facture["client_id"])
        total = get_total_price(facture)
        restant = total - get_total_deposits(facture)
        path = "/formulaire/gff/" + str(factureId)
    elif devisId != None:
        devis = estimate_mng.read_estimate(devisId)
        client = client_mng.read_client(devis["client_id"])
        total = get_total_price(devis)
        path = "/formulaire/gfd/" + str(devisId)
    
    #if request, post, contient import client, then import client
    if request.method == 'POST':
        r = getformulaireForm(request.form)
        print(r)
        if "pdf" in r:
            no_header = 1
        else:
            if r == 'None':
                client = None
            else:
                client = client_mng.read_client(int(r))

    if artisan["template_selected"] == "STYLE2":
        return render_template("formulaire1.html",
                                PATH = path,
                                ARTISAN = artisan,
                                CLIENT = client,
                                CLIENTS = clients,
                                FACTURE = facture,
                                DEVIS = devis,
                                TOTAL = total,
                                RESTANT = restant,
                                NO_HEADER = no_header)

    elif artisan["template_selected"] == "STYLE3":
        return render_template("formulaire2.html",
                                PATH = path,
                                ARTISAN = artisan,
                                CLIENT = client,
                                CLIENTS = clients,
                                FACTURE = facture,
                                DEVIS = devis,
                                TOTAL = total,
                                RESTANT = restant,
                                NO_HEADER = no_header)
    else:
        return render_template("formulaire.html",
                                PATH = path,
                                ARTISAN = artisan,
                                CLIENT = client,
                                CLIENTS = clients,
                                FACTURE = facture,
                                DEVIS = devis,
                                TOTAL = total,
                                RESTANT = restant,
                                NO_HEADER = no_header)