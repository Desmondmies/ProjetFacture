"""
data: dict of class instance
"""
from Python.Estimate import Estimate
from Python.Invoice import Invoice


def search_by_name(data: dict, name_value: str) -> list:
	search_res = []

	for id, obj in data.items():
		if isinstance(obj, Estimate) or isinstance(obj, Invoice):
			obj = obj["client"]

		if name_value in obj.surname or name_value in obj.firstname:
			search_res.append(obj)

	return search_res

def search_by_address(data: dict, address_value: str) -> list:
	search_res = []

	for id, obj in data.items():
		if isinstance(obj, Estimate) or isinstance(obj, Invoice):
			obj = obj["client"]

		if address_value in obj.adress:
			search_res.append(obj)

	return search_res

def search_by_tel(data: dict, tel_value: str) -> list:
	search_res = []

	for id, obj in data.items():
		if isinstance(obj, Estimate) or isinstance(obj, Invoice):
			obj = obj["client"]

		if tel_value in obj.phone:
			search_res.append(obj)

	return search_res
