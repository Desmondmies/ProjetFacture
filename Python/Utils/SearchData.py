"""
data: dict of class instance
"""
from Python.Estimate import Estimate
from Python.Invoice import Invoice

cl_mng = None

def set_client_manager(cl):
	global cl_mng
	cl_mng = cl

def search_by_name(data: dict, name_value: str) -> dict:
	search_res = {}

	for id, obj in data.items():
		tmp = obj
		if isinstance(obj, Estimate) or isinstance(obj, Invoice):
			tmp = cl_mng.read_client( obj["client_id"] )

		if name_value.upper() in tmp["surname"].upper() or name_value.upper() in tmp["firstname"].upper():
			search_res[id] = obj

	return search_res

def search_by_address(data: dict, address_value: str) -> dict:
	search_res = {}

	for id, obj in data.items():
		if isinstance(obj, Estimate) or isinstance(obj, Invoice):
			obj = cl_mng.read_client( obj["client_id"] )

		if address_value.upper() in obj["adress"].upper() or address_value.upper() in str(obj["postcode"]):
			search_res[id] = obj

	return search_res

def search_by_tel(data: dict, tel_value: str) -> dict:
	search_res = {}

	for id, obj in data.items():
		if isinstance(obj, Estimate) or isinstance(obj, Invoice):
			obj = cl_mng.read_client( obj["client_id"] )

		if tel_value.upper() in str(obj["phone"]):
			search_res[id] = obj

	return search_res
