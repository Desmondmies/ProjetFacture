from flask import render_template, request, redirect, url_for

from Python.Manager.Invoice_mng import invoice_mng
from Python.Manager.Client_mng import client_mng
from Python.Manager.Artisan import artisan

from Python.FormRequestHandlers.CardFormRequest import getcardForm

def add_facture_page_ctrl():
    if request.method == 'POST':
        r = getcardForm(request.form)
        info = r.split('¤')
        if "ADD_" in info[0]:
            add_facture(info)
            return redirect(url_for("facture_route"))

    client_all = client_mng.dict_clients
    
    return render_template("add_facture.html",
                            PATH = "/add_facture",
                            CLIENTS = client_all)

def add_facture(info):
    tmp = ("client_id","creation_date","due_date", "comment","acquitted","list_items")
    dico = {}
    for i in range(0,len(tmp)):
        print(tmp[i], info[i+1])
        if i < len(tmp)-1: 
            dico[tmp[i]] = info[i+1]
        else:
            print(info[i:])
            dico[tmp[i]] = info[i+1:]
    dico["artisan"] = artisan.data
    invoice_mng.create_invoice(dico)