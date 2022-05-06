from flask import render_template, request, redirect, url_for

from Python.Manager.Estimate_mng import estimate_mng
from Python.Manager.Client_mng import client_mng

from Python.FormRequestHandlers.CardFormRequest import getcardForm

def modify_devis_page_ctrl(devis_id):
    if request.method == 'POST':
        r = getcardForm(request.form)
        info = r.split('¤')
        print(info)
        if "MODIFY_" in info[0]:
            modify_devis(devis_id, info)
            return redirect(url_for("devis_route"))
        
    devis = estimate_mng.read_estimate(devis_id)
    client_all = client_mng.dict_clients

    return render_template("modify_devis.html",
                            DATA = devis,
                            PATH = "/modify_devis/" + str(devis_id),
                            CLIENTS = client_all)

def modify_devis(id, info):
    devis = estimate_mng.read_estimate(id)
    keys = ("client_id","creation_date", "comment","list_items")
    for i in range(0,len(keys)):
        if keys[i] != "list_items":
            if devis[keys[i]] == info[i+1]:
                continue
            estimate_mng.update_estimate(id, keys[i], info[i+1])
        else:
            l = info[i+1:]
            if devis[keys[i]] == l:
                continue
            estimate_mng.update_estimate(id, keys[i], l)
        