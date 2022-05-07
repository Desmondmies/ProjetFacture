from flask import render_template, request, redirect, url_for

from Python.Manager.Estimate_mng import estimate_mng
from Python.Manager.Client_mng import client_mng

from Python.FormRequestHandlers.CardFormRequest import getcardForm
from Python.Utils.check_data import check_estimate

def modify_devis_page_ctrl(devis_id):
    error_flags = []

    if request.method == 'POST':
        r = getcardForm(request.form)
        info = r.split('¤')
        print(info)
        if "MODIFY_" in info[0]:
            success = modify_devis(devis_id, info)
            if success == 1:
                return redirect(url_for("devis_route"))
            else:
                error_flags = success
        
    devis = estimate_mng.read_estimate(devis_id)
    client_all = client_mng.dict_clients

    return render_template("modify_devis.html",
                            DATA = devis,
                            PATH = "/modify_devis/" + str(devis_id),
                            CLIENTS = client_all,
                            ERROR_FLAGS = error_flags)

def modify_devis(id, info):
    devis = estimate_mng.read_estimate(id)
    keys = ("client_id","creation_date", "comment","list_items")
    for i in range(0,len(keys)):
        if keys[i] == "list_items":
            d_items = get_list_item(i, info)
            if devis[keys[i]] == d_items:
                continue
            estimate_mng.update_estimate(id, keys[i], d_items)
        else:
            tmp_info = info[i+1]
            if i == 0: tmp_info = int(tmp_info)
            if devis[keys[i]] == tmp_info:
                continue
            estimate_mng.update_estimate(id, keys[i], info[i+1])

    devis = estimate_mng.read_estimate(id)
    e = check_estimate(devis)
    if len(e) != 0:
        return e
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
        