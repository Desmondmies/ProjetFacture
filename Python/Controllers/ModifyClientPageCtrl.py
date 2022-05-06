from flask import redirect, render_template, request, url_for

from Python.Manager.Client_mng import client_mng

from Python.FormRequestHandlers.CardFormRequest import getcardForm

def modify_client_page_ctrl(client_id):
    if request.method == 'POST':
        r = getcardForm(request.form)
        info = r.split('¤')
        if "MODIFY_" in info[0]:
            modify_client(client_id, info)
            return redirect(url_for("client_route"))
        
    client = client_mng.read_client(client_id)
    
    return render_template("modify_client.html",
                            DATA = client,
                            PATH = "/modify_client/" + str(client_id))

def modify_client(id, info):
    client = client_mng.read_client(id)
    keys = ("surname","firstname","adress", "postcode","mail","phone","description")
    for i in range(1,len(info)):
        if client[keys[i-1]] == info[i]:
            continue
        client_mng.update_client(id, keys[i-1], info[i])