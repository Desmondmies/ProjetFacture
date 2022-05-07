from flask import render_template, request, redirect, url_for

from Python.Manager.Estimate_mng import estimate_mng
from Python.Manager.Client_mng import client_mng

from Python.FormRequestHandlers.CardFormRequest import getcardForm

from Python.Utils.check_data import check_estimate

def add_devis_page_ctrl(clientId = None):
    error_flags = []

    client_selected = None

    if clientId != None:
        client_selected = clientId

    if request.method == 'POST':
        r = getcardForm(request.form)
        info = r.split('¤')
        if "ADD_" in info[0]:
            success = add_devis(info)
            if success == 1:
                return redirect(url_for("devis_route"))
            else:
                error_flags = success

    client_all = client_mng.dict_clients
    
    return render_template("add_devis.html",
                            PATH = "/add_devis",
                            CLIENTS = client_all,
                            ERROR_FLAGS = error_flags,
                            CLIENT_SELECTED = client_selected)

def add_devis(info):
    tmp = ("client_id","creation_date", "comment","list_items")
    dico = {}
    for i in range(0,len(tmp)):
        if tmp[i] == "list_items":
            dico[tmp[i]] = get_list_item(i, info)
        else:
            tmp_info = info[i+1]
            if i == 0: tmp_info = int(tmp_info)
            dico[tmp[i]] = tmp_info

    e = check_estimate(dico)
    if len(e) != 0:
        return e
    estimate_mng.create_estimate(dico)
    return 1

def get_list_item(idx, info) -> list:
    l_item = []
    new_idx = idx+1
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