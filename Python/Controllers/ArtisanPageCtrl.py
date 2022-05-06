from flask import render_template, request, redirect, url_for

from Python.Manager.Artisan import artisan

from Python.FormRequestHandlers.ArtisanFormRequest import getartisanForm
from Python.Utils.GetFilterIndex import get_new_search_filter_index

def artisan_page_ctrl():
    if request.method == 'POST':
        r = getartisanForm(request.form)
        print(r)

        if "¤" in r :
            info = r.split('¤')
            tmp = ("compagny_name","surname","firstname","adress","mail_compagny","phone", "template_selected")
            for i in range(1,len(info)):
                #clé du dico dans tmp et valeur vient d'artisan
                artisan[tmp[i-1]]=info[i]

    return render_template("artisan.html",
                            TEMPLATE_ID="Artisan",
                            ARTISAN= artisan,
                            PATH="/artisan",
                            SEARCH_BAR=False )