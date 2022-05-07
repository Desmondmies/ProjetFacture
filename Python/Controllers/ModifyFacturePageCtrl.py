from flask import render_template, request, redirect, url_for

from Python.Manager.Invoice_mng import invoice_mng
from Python.Manager.Client_mng import client_mng

from Python.FormRequestHandlers.CardFormRequest import getcardForm
from Python.Utils.check_data import check_invoice
from Python.Utils.SumItemsDeposits import IsTotalPaid

def modify_facture_page_ctrl(facture_id):
    error_flags = []

    if request.method == 'POST':
        r = getcardForm(request.form)
        info = r.split('¤')
        if "MODIFY_" in info[0]:
            success = modify_facture(facture_id, info)
            if success == 1:
                return redirect(url_for("facture_route"))
            else:
                error_flags = success
        
    facture = invoice_mng.read_invoice(facture_id)
    client_all = client_mng.dict_clients

    return render_template("modify_facture.html",
                            DATA = facture,
                            PATH = "/modify_facture/" + str(facture_id),
                            CLIENTS = client_all,
                            ERROR_FLAGS = error_flags)

def modify_facture(id, info):
    facture = invoice_mng.read_invoice(id)
    keys = ("client_id","creation_date", "due_date", "comment", "list_deposits", "list_items")
    for i in range(0,len(keys)):
        if keys[i] == "list_items":
            l_items = get_list_item(i, info)
            if facture[keys[i]] == l_items:
                continue
            invoice_mng.update_invoice(id, keys[i], l_items)
        elif keys[i] == "list_deposits":
            l_items = get_list_deposit(i, info)
            if facture[keys[i]] == l_items:
                continue
            invoice_mng.update_invoice(id, keys[i], l_items)
        else:
            tmp_info = info[i+1]
            if i == 0: tmp_info = int(tmp_info)
            if facture[keys[i]] == tmp_info:
                continue
            invoice_mng.update_invoice(id, keys[i], info[i+1])
    
    facture = invoice_mng.read_invoice(id)

    paid_or_not = int( IsTotalPaid(facture) )
    invoice_mng.update_invoice(id, "acquitted", paid_or_not)

    e = check_invoice(facture)
    if len(e) != 0:
        return e
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
        new_idx += 4
        if i_nom != '':
            d["name"] = i_nom
        if i_desc != '':
            d["description"] = i_desc
        if i_quant != '':
            d["quantity"] = int(i_quant)
        if i_price != '':
            d["price"] = int(i_price)
        l_item.append(d)
    return l_item
        