from flask import render_template, request, redirect, url_for

from Python.Manager.Invoice_mng import invoice_mng
from Python.Manager.Estimate_mng import estimate_mng
from Python.Manager.Client_mng import client_mng

from Python.FormRequestHandlers.CardFormRequest import getcardForm
from Python.Utils.check_data import check_invoice
from Python.Utils.SumItemsDeposits import IsTotalPaid

def add_facture_page_ctrl(clientId = None, devisId = None):
    error_flags = []

    client_selected = None
    devis = None

    #add id client de base, if coming from générer facture, ajout variable CLIENT_SELECTED = None dans render template
    if clientId != None:
        client_selected = clientId
    elif devisId != None:
        devis = estimate_mng.read_estimate(devisId)
        client_selected = devis["client_id"]

    if request.method == 'POST':
        r = getcardForm(request.form)
        info = r.split('¤')
        if "ADD_" in info[0]:
            success = add_facture(info)
            if success == 1:
                return redirect(url_for("facture_route"))
            else:
                error_flags = success

    client_all = client_mng.dict_clients
    
    return render_template("add_facture.html",
                            PATH = "/add_facture",
                            CLIENTS = client_all,
                            ERROR_FLAGS = error_flags,
                            CLIENT_SELECTED = client_selected,
                            DEVIS = devis)

def add_facture(info):
    tmp = ("client_id","creation_date","due_date", "comment","list_deposits", "list_items")
    dico = {}
    for i in range(0,len(tmp)):
        if tmp[i] == "list_items": 
            dico[tmp[i]] = get_list_item(i, info)
        elif tmp[i] == "list_deposits":
            dico[tmp[i]] = get_list_deposit(i, info)
        else:
            tmp_info = info[i+1]
            if i == 0: tmp_info = int(tmp_info)
            dico[tmp[i]] = tmp_info  
    
    dico["acquitted"] = int( IsTotalPaid(dico) )

    e = check_invoice(dico)
    if len(e) != 0:
        return e
    invoice_mng.create_invoice(dico)
    return 1

def get_list_deposit(idx, info) -> list:
    l_dep = []
    new_idx = idx + 1
    for j in range(0, 5):
        d = {}
        i_date = info[new_idx]
        i_somme = info[new_idx + 1]
        new_idx += 2
        d["payment_date"] = i_date
        if i_somme != '':
            d["amount"] = int(i_somme)
        l_dep.append(d)
    return l_dep

def get_list_item(idx, info) -> list:
    l_item = []
    new_idx = idx+10
    for j in range(0, 10):
        d = {}
        i_nom = info[new_idx]
        i_desc = info[new_idx+1]
        i_quant = info[new_idx+2]
        i_price = info[new_idx+3]
        if i_nom != '':
            d["name"] = i_nom
        if i_desc != '':
            d["description"] = i_desc
        if i_quant != '':
            d["quantity"] = int(i_quant)
        if i_price != '':
            d["price"] = int(i_price)
        l_item.append(d)
        new_idx += 4
    return l_item