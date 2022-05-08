from flask import render_template, request
from datetime import date

from Python.FormRequestHandlers.FormulaireFormRequest import getformulaireForm

from Python.Manager.Artisan import artisan
from Python.Manager.Invoice_mng import invoice_mng
from Python.Manager.Estimate_mng import estimate_mng
from Python.Manager.Client_mng import client_mng

from Python.Utils.SumItemsDeposits import get_total_price, get_total_deposits, get_remaining_amount

def formulaire_page_ctrl(factureId = None, devisId = None):

    facture, devis, client = None, None, None
    total = None
    restant = None
    no_header = None
    rendu = None

    path = "/formulaire"

    clients = client_mng.dict_clients

    if factureId != None:
        facture = invoice_mng.read_invoice(factureId)
        client = client_mng.read_client(facture["client_id"])
        total = get_total_price(facture)
        restant = get_remaining_amount(facture)
        path = "/formulaire/gff/" + str(factureId)
    elif devisId != None:
        devis = estimate_mng.read_estimate(devisId)
        client = client_mng.read_client(devis["client_id"])
        total = get_total_price(devis)
        path = "/formulaire/gfd/" + str(devisId)
    
    #if request, post, contient import client, then import client
    if request.method == 'POST':
        r = getformulaireForm(request.form)
        if "RENDU¤" in r:
            no_header = 1
            info = r.split('¤')
            rendu = {}
            rendu["client"] = get_client_for_rendu(info)
            if len(client_mng.search_client(rendu["client"]["phone"])) == 0:
                client_mng.create_client(rendu["client"])

            if factureId != None:
                rendu["creation_date"] = get_creation_date_for_rendu(info)
                rendu["due_date"] = get_due_date_for_rendu(info)
                rendu["list_items"] = get_prod_for_rendu_f(info)
                rendu["list_deposits"] = get_deposits_for_rendu(info)
                total = get_total_price(rendu)
                restant = get_remaining_amount(rendu)
            elif devisId != None:
                rendu["creation_date"] = get_creation_date_for_rendu(info)
                rendu["list_items"] = get_prod_for_rendu_d(info)
                total = get_total_price(rendu)
            else:
                rendu["creation_date"] = get_creation_date_for_rendu(info)
                rendu["due_date"] = get_due_date_for_rendu(info)
                rendu["list_items"] = get_prod_for_rendu_f(info)
                rendu["list_deposits"] = get_deposits_for_rendu(info)
                total = get_total_price(rendu)
                restant = get_remaining_amount(rendu)
            
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
                                NO_HEADER = no_header,
                                RENDU = rendu)

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
                                NO_HEADER = no_header,
                                RENDU = rendu)
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
                                NO_HEADER = no_header,
                                RENDU = rendu)

def get_client_for_rendu(info):
    res = {}
    keys = ['surname', 'firstname', 'phone', 'adress', 'mail']
    for i in range(5):
        res[keys[i]] = info[i+1]

    if len(res) == 0:
        return None

    res["description"] = ""
    res["postcode"] = "00000"
    return res

def get_creation_date_for_rendu(info):
    da = info[6]
    if len(da) == 0 or da == '':
        return str(date.today())
    return da

def get_due_date_for_rendu(info):
    da = info[7]
    if len(da) == 0 or da == '':
        return str(date.today())
    return da

def get_deposits_for_rendu(info):
    res = []
    idx = 8
    for i in range(5):
        date = info[idx]
        somme = info[idx+1]
        idx += 2

        d = {"payment_date": date}
        if somme != '':
            d["amount"] = int(somme)
        res.append(d)
    
    if len(res) == 0:
        return None
    return res

def get_prod_for_rendu_f(info):
    res = []
    idx = 18
    for i in range(10):
        n = info[idx]
        q = info[idx+1]
        p = info[idx+2]
        idx += 3
        d = {"name": n}
        if q != '':
           d["quantity"] = int(q)
        if p != '':
            d["price"] = int(p)
       
        res.append(d)
    
    if len(res) == 0:
        return None
    return res

def get_prod_for_rendu_d(info):
    res = []
    idx = 7
    for i in range(10):
        n = info[idx]
        q = info[idx+1]
        p = info[idx+2]
        idx += 3
        d = {"name": n}
        if q != '':
           d["quantity"] = int(q)
        if p != '':
            d["price"] = int(p)
        res.append(d)
    
    if len(res) == 0:
        return None
    return res