from flask import render_template, request, redirect, url_for

from Python.Manager.Client_mng import client_mng

from Python.FormRequestHandlers.ClientFormRequest import getclientForm
from Python.Utils.GetFilterIndex import get_new_search_filter_index

filter_btn_toggle = False

def client_page_ctrl(searchedId = None):
    global filter_btn_toggle

    client_data = client_mng.dict_clients

    if searchedId != None:
        client_data = {}
        client_data[searchedId] = client_mng.read_client(searchedId)

    if request.method == 'POST':
        r = getclientForm(request.form)
        print(r)
        if r == "FILTER":
            # clic sur le bouton filtre de la barre de recherche
            filter_btn_toggle = not filter_btn_toggle
        elif "Filter_" in r:
            # changement du filtre de la barre de recherche
            filter_idx = get_new_search_filter_index(r)
            client_mng.change_search_filter(filter_idx)
        elif r == "ADD":
            #clic sur le bouton add
            return redirect(url_for("add_client_route"))
        elif "Rechercher" in r:
            #barre de recherche sur client
            search_value = r.split('¤')
            if len(search_value) >= 2:
                client_data = client_mng.search_client(search_value[1])
        elif "Gen_Facture" in r:
            id = r.split('¤')[1]
            return redirect(url_for("add_facture_fromClient_route", id=id))
        elif "Gen_Devis" in r:
            id = r.split('¤')[1]
            return redirect(url_for("add_devis_fromClient_route", id=id))
        elif "Modifier" in r:
            id = r.split('¤')[1]
            #modifier client avec les infos du client à cette id
            return redirect(url_for("modify_client_route", id = id))
        elif "Supprimer" in r:
            id = r.split('¤')[1]
            client_mng.delete_client(int(id))

    #posts = variable à passer en paramètre à notre page HTML
    return render_template("client.html",
                            CLIENTS_DATA = client_data,
                            TEMPLATE_ID="Client",
                            PATH="/client",
                            SEARCH_BAR=True,
                            FILTER_TOGGLE = filter_btn_toggle,
                            SEARCH_IDX = client_mng.search_filter_index)