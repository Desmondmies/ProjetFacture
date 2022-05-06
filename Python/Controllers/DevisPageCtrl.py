from flask import render_template, request, redirect, url_for

from Python.Manager.Estimate_mng import estimate_mng
from Python.Manager.Client_mng import client_mng

from Python.FormRequestHandlers.DevisFormRequest import getdevisForm
from Python.Utils.GetFilterIndex import get_new_search_filter_index

filter_btn_toggle = False

def devis_page_ctrl():
    global filter_btn_toggle

    devis_all = estimate_mng.dict_estimates

    if request.method == 'POST':
        r = getdevisForm(request.form)
        print(r)
        if r == "FILTER":
            filter_btn_toggle = not filter_btn_toggle
        elif "Filter_" in r:
            filter_idx = get_new_search_filter_index(r)
            estimate_mng.change_search_filter(filter_idx)
        elif r == "ADD":
            #clic sur le bouton add
            return redirect(url_for("add_devis_route"))
        elif "Rechercher" in r:
            search_value = r.split('¤')
            if len(search_value) >= 2:
                devis_all = estimate_mng.search_client(search_value[1])
        elif "ConvertToFormulaire" in r:
            id = r.split('¤')[1]
            #redirect to formulaire avec id devis en parametre
            pass
        elif "Voir Client" in r:
            id = r.split('¤')[1]
            #redirect à page client avec recherche sur id si possible?
            pass
        elif "Modifier" in r:
            id = r.split('¤')[1]
            #modifier client avec les infos du client à cette id
            return redirect(url_for("modify_devis_route", id = id))
        elif "Supprimer" in r:
            id = r.split('¤')[1]
            estimate_mng.delete_estimate(int(id))

    client_all = get_all_clients_from_devis(devis_all)
    data = get_devisclient_list(devis_all, client_all)

    return render_template("devis.html",
                            DATA = data,
                            TEMPLATE_ID="Devis",
                            PATH="/devis",
                            SEARCH_BAR=True,
                            FILTER_TOGGLE = filter_btn_toggle,
                            SEARCH_IDX = estimate_mng.search_filter_index)

def get_all_clients_from_devis(devis_dict):
    all_clients = []
    for devis in devis_dict.values():
        all_clients.append( client_mng.read_client( int(devis["client_id"]) ) )
    
    return all_clients

def get_devisclient_list(devis, client):
    all = []
    for d, c in zip(devis.values(), client):
        all.append((d, c))
    return all