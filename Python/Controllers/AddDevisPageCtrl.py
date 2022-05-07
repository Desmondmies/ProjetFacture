from flask import render_template, request, redirect, url_for

from Python.Manager.Estimate_mng import estimate_mng
from Python.Manager.Client_mng import client_mng
from Python.Manager.Artisan import artisan

from Python.FormRequestHandlers.CardFormRequest import getcardForm

def add_devis_page_ctrl():
    if request.method == 'POST':
        r = getcardForm(request.form)
        info = r.split('¤')
        if "ADD_" in info[0]:
            add_devis(info)
            return redirect(url_for("devis_route"))

    client_all = client_mng.dict_clients
    
    return render_template("add_devis.html",
                            PATH = "/add_devis",
                            CLIENTS = client_all)

def add_devis(info):
    tmp = ("client_id","creation_date", "comment","acquitted","list_items")
    dico = {}
    for i in range(0,len(tmp)):
        if i < len(tmp)-1: 
            dico[tmp[i]] = info[i+1]
        else:
            dico[tmp[i]] = info[i+1:]
    dico["artisan"] = artisan.data
    estimate_mng.create_estimate(dico)