from flask import render_template, request, redirect, url_for

from Python.Manager.Invoice_mng import invoice_mng
from Python.Manager.Client_mng import client_mng

from Python.FormRequestHandlers.CardFormRequest import getcardForm

def modify_facture_page_ctrl(facture_id):
    if request.method == 'POST':
        r = getcardForm(request.form)
        info = r.split('¤')
        if "MODIFY_" in info[0]:
            modify_facture(facture_id, info)
            return redirect(url_for("facture_route"))
        
    facture = invoice_mng.read_invoice(facture_id)
    client_all = client_mng.dict_clients

    return render_template("modify_facture.html",
                            DATA = facture,
                            PATH = "/modify_facture/" + str(facture_id),
                            CLIENTS = client_all)

def modify_facture(id, info):
    facture = invoice_mng.read_invoice(id)
    keys = ("client_id","creation_date", "due_date", "comment","acquitted","list_items")
    for i in range(0,len(keys)):
        if keys[i] != "list_items":
            if facture[keys[i]] == info[i+1]:
                continue
            invoice_mng.update_invoice(id, keys[i], info[i+1])
        else:
            l = info[i+1:]
            if facture[keys[i]] == l:
                continue
            invoice_mng.update_invoice(id, keys[i], l)
        