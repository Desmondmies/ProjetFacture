from Python.Estimate import Estimate
from Python.Invoice import Invoice

cl_mng = None

def set_client_manager(cl):
	global cl_mng
	cl_mng = cl

def check_name(data: dict, value: str) -> bool:
	return value.upper() in data["surname"].upper() or value.upper() in data["firstname"].upper()

def check_adress(data: dict, value: str) -> bool:
	return value.upper() in data["adress"].upper() or value.upper() in str(data["postcode"])

def check_phone(data: dict, value: str) -> bool:
	return value.upper().replace(" ", '') in str(data["phone"]).replace(" ", '')
	
def check_mail(data: dict, value: str) -> bool:
	return value.upper() in data["mail"].upper()

def search_by_name(data: dict, name_value: str) -> dict:
	search_res = {}

	for id, obj in data.items():
		tmp = obj
		if isinstance(obj, Estimate) or isinstance(obj, Invoice):
			tmp = cl_mng.read_client( obj["client_id"] )

		if tmp == None: continue
		if check_name(tmp, name_value):
			search_res[id] = obj
	return search_res

def search_by_address(data: dict, address_value: str) -> dict:
	search_res = {}

	for id, obj in data.items():
		tmp = obj
		if isinstance(obj, Estimate) or isinstance(obj, Invoice):
			tmp = cl_mng.read_client( obj["client_id"] )

		if tmp == None: continue
		if check_adress(tmp, address_value):
			search_res[id] = obj
	return search_res

def search_by_tel(data: dict, tel_value: str) -> dict:
	search_res = {}

	for id, obj in data.items():
		tmp = obj
		if isinstance(obj, Estimate) or isinstance(obj, Invoice):
			tmp = cl_mng.read_client( obj["client_id"] )

		if tmp == None: continue
		if check_phone(tmp, tel_value):
			search_res[id] = obj
	return search_res

def search_by_mail(data: dict, mail_value: str) -> dict:
	search_res = {}

	for id, obj in data.items():
		tmp = obj
		if isinstance(obj, Estimate) or isinstance(obj, Invoice):
			tmp = cl_mng.read_client( obj["client_id"] )

		if tmp == None: continue
		if check_mail(tmp, mail_value):
			search_res[id] = obj
	return search_res

def search_all(data: dict, search_value: str) -> dict:
	search_res = {}

	for id, obj in data.items():
		tmp = obj
		if isinstance(obj, Estimate) or isinstance(obj, Invoice):
			tmp = cl_mng.read_client( obj["client_id"] )

		if tmp == None: continue
		if check_name(tmp, search_value) or check_adress(tmp, search_value) or check_phone(tmp, search_value) or check_mail(tmp, search_value):
			search_res[id] = obj
	return search_res

def search(data: dict, filter_idx: int, search_value: str) -> dict:
	res = {}

	if filter_idx == -1:
		res = search_all(data, search_value)
	elif filter_idx == 0:
		res = search_by_name(data, search_value)
	elif filter_idx == 1:
		res = search_by_address(data, search_value)
	elif filter_idx == 2:
		res = search_by_tel(data, search_value)
	elif filter_idx == 3:
		res = search_by_mail(data, search_value)
	return res