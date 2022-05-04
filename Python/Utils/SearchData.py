"""
data: dict of class instance
"""
def search_by_name(data: dict, name_value: str) -> list:
	search_res = []

	for id, obj in data.items():
		if name_value in obj.surname or name_value in obj.firstname:
			search_res.append(obj)

	return search_res

def search_by_address(data: dict, address_value: str) -> list:
	search_res = []

	for id, obj in data.items():
		if name_value in obj.adress:
			search_res.append(obj)

	return search_res

def search_by_tel(data: dict, tel_value: str) -> list:
	search_res = []

	for id, obj in data.items():
		if name_value in obj.phone:
			search_res.append(obj)

	return search_res
