from flask import render_template, request, redirect, url_for

from Python.Manager.Client_mng import client_mng

from Python.FormRequestHandlers.CardFormRequest import getcardForm

def add_client_page_ctrl():
    if request.method == 'POST':
        r = getcardForm(request.form)
        info = r.split('¤')
        if "ADD_" in info[0]:
            add_client(info)
            return redirect(url_for("client_route"))
    
    return render_template("add_client.html",
                            PATH = "/add_client")

def add_client(info):
    tmp = ("surname","firstname","adress", "postcode","mail","phone","description")
    dico = {}
    for i in range(1,len(info)):
        dico[tmp[i-1]]=info[i]
    client_mng.create_client(dico)