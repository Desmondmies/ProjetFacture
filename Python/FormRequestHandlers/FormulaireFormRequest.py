form_keys = ['s_client', 'btn_rendupdf']

def getformulaireForm(form):
    if form_keys[1] in form:
        return form['btn_rendupdf']
    elif form_keys[0] in form:
        return form['s_client']
    raise KeyError("NO FORM MATCHING KEYS")