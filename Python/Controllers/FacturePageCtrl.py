from flask import render_template, request, redirect, url_for

from Python.Manager.Invoice_mng import invoice_mng
from Python.Manager.Client_mng import client_mng

from Python.FormRequestHandlers.FactureFormRequest import getfactureForm
from Python.Utils.GetFilterIndex import get_new_search_filter_index

filter_btn_toggle = False

def facture_page_ctrl():
    global filter_btn_toggle

    facture_all = invoice_mng.dict_invoices

    if request.method == 'POST':
        r = getfactureForm(request.form)
        print(r)
        if r == "FILTER":
            filter_btn_toggle = not filter_btn_toggle
        elif "Filter_" in r:
            filter_idx = get_new_search_filter_index(r)
            invoice_mng.change_search_filter(filter_idx)
        elif r == "ADD":
            #clic sur le bouton add
            return redirect(url_for("add_facture_route"))
        elif "Rechercher" in r:
            search_value = r.split('¤')
            if len(search_value) >= 2:
                facture_all = invoice_mng.search_client(search_value[1])
        elif "ConvertToFormulaire" in r:
            id = r.split('¤')[1]
            return redirect(url_for("formulaire_fromFacture_route", factId = id))
        elif "Voir Client" in r:
            id = r.split('¤')[1]
            fact = invoice_mng.read_invoice(int(id))
            return redirect(url_for("client_searched_route", id=fact["client_id"]))
        elif "Modifier" in r:
            id = r.split('¤')[1]
            #modifier client avec les infos du client à cette id
            return redirect(url_for("modify_facture_route", id = id))
        elif "Supprimer" in r:
            id = r.split('¤')[1]
            invoice_mng.delete_invoice(int(id))

    client_all = get_all_clients_from_facture(facture_all)
    data = get_factureclient_list(facture_all, client_all)

    #return à la bonne page en fonction du btn bandeau == "Voir Client" ou autre
    return render_template("facture.html",
                            DATA = data,
                            TEMPLATE_ID="Facture",
                            PATH="/facture",
                            SEARCH_BAR=True,
                            FILTER_TOGGLE= filter_btn_toggle,
                            SEARCH_IDX=invoice_mng.search_filter_index)

def get_all_clients_from_facture(facture_dict):
    all_clients = []
    for facture in facture_dict.values():
        all_clients.append( client_mng.read_client( int(facture["client_id"]) ) )
    
    return all_clients

def get_factureclient_list(facture, client):
    all = []
    for d, c in zip(facture.values(), client):
        all.append((d, c))
    return all