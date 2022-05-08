from flask import render_template, request

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
            if factureId != None:
                rendu["due_date"] = get_due_date_for_rendu(info)
                rendu["list_items"] = get_prod_for_rendu_f(info)
                rendu["list_deposits"] = get_deposits_for_rendu(info)
                total = get_total_price(facture)
                restant = get_remaining_amount(facture)
            elif devisId != None:
                rendu["list_items"] = get_prod_for_rendu_d(info)
                total = get_total_price(devis)            
            
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
    return res

def get_due_date_for_rendu(info):
    date = info[6]
    if len(date) == 0 or date == '':
        return None
    return date

def get_deposits_for_rendu(info):
    res = []
    idx = 7
    for i in range(5):
        d = {}
        date = info[idx]
        somme = info[idx+1]
        idx += 2
        d[i] = {"payment_date": date, "amount": somme}
        res.append(d)
    
    if len(res) == 0:
        return None
    return res

def get_prod_for_rendu_f(info):
    res = []
    idx = 17
    for i in range(10):
        d = {}
        name = info[idx]
        quant = info[idx+1]
        price = info[idx+2]
        idx += 3
        d[i] = {"name": name,"quantity": quant, "price":price}
        res.append(d)
    
    if len(res) == 0:
        return None
    return res

def get_prod_for_rendu_d(info):
    res = []
    idx = 6
    for i in range(10):
        d = {}
        name = info[idx]
        quant = info[idx+1]
        price = info[idx+2]
        idx += 3
        d[i] = {"name": name,"quantity": quant, "price":price}
        res.append(d)
    
    if len(res) == 0:
        return None
    return res