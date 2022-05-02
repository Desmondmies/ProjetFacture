form_keys = ['bandeau_btn',
            'searchbar_btn',
            'add_btn',
			'filter_btn',
			'search_filter']

def getclientForm(form):
	for key in form_keys:
		if key in form:
			return form[key]
	raise KeyError("NO FORM MATCHING KEYS")