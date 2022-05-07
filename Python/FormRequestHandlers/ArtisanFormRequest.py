form_keys = ['bandeau_btn',
            'searchbar_btn',
            'add_btn',
            'save_artisan',
            'choice_style']

def getartisanForm(form):
    for key in form_keys :
        if key in form :
            return form[key]
    raise KeyError("NO FORM MATCHING KEYS")
