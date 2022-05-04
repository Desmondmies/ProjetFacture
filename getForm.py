form_keys = ['bandeau_btn',
            'searchbar_btn',
            'add_btn',
            'save_artisan',
            'save_client',
            'choice_style']

def getForm(form):
    for key in form_keys :
        if key in form :
            return form[key]
    print("TEST" , form)

    raise KeyError("NO FORM MATCHING KEYS")
