import os
import json

from Python.Client import Client
from Python.Utils.SearchData import search_by_name, search_by_address, search_by_tel

clients_path = os.path.abspath("./JSON/Clients.json")

class Client_mng:
	def __init__(self) -> None:
		self.dict_clients = {} #Les numéros client sont les clés et les valeurs sont une instance de Client
		self.init_dict_clients()

		self.update_newClient_id()

		self.search_filter_index = 0
		return

	"""
	Initialisation du dictionnaire des clients présents dans le fichier "./JSON/Clients.json".
	On charge le fichier en question puis on convertit chaque données des clients en instance de Client que l'on stocke dans le dictionnaire des clients.
	"""
	def init_dict_clients(self) -> None:
			fd = open(clients_path, "r")
			dict_data_clients = json.load(fd)
			fd.close()

			for client_id, dict_data_client in dict_data_clients.items():
				self.dict_clients[int(client_id)] = Client(dict_data_client)
			return

	def update_newClient_id(self) -> None:
		if len(self.dict_clients) == 0:
			self.newClient_id = 0
		else:
			self.newClient_id = max(self.dict_clients) + 1 #Numéro du prochain client à créer : pas en fonction du nombre de clients car un dictionnaire de mille clients ne signifie pas que le dernier client a le numéro 1000

	"""
	On créé une instance de client puis on met à jour le dictionnaire des cients existants, le fichier json et le numéro du prochain client
	"""
	def create_client(self, dict_data_client) -> None:
		"""

		"""
		dict_data_client["id"] = self.newClient_id #On rajoute le numéro du nouveau client
		self.dict_clients[self.newClient_id] = Client(dict_data_client)

		#On charge les données des clients stockées dans le fichier Clients.json
		fd = open(clients_path, "r")
		clients_json = json.load(fd)
		fd.close()

		#On rajoute les données du client dans le fichier Clients.json puis on sauvegarde
		clients_json[str(self.newClient_id)] = dict_data_client
		fd = open(clients_path, "w")
		json.dump(clients_json, fd)
		fd.close()

		self.newClient_id += 1
		return

	"""
	Renvoie toutes les données concernant un client
	"""
	def read_client(self, client_id) -> Client:
		return self.dict_clients[client_id]["all"] #"all" est un mot clé créé pour récupérer les données d'un client

	"""
	Permet de modifier les informations d'un client stockée grâce à son numéro client, du nom de l'attribut et de la nouvelle valeur
	"""
	def update_client(self, client_id:int, attribute:str, new_val) -> None:
		self.dict_clients[client_id][attribute] = new_val

		#On charge les données des clients stockées dans le fichier Clients.json
		fd = open(clients_path, "r")
		clients_json = json.load(fd)
		fd.close()

		#On modifie les données du client dans le fichier Clients.json puis on sauvegarde
		clients_json[str(client_id)][attribute] = new_val
		fd = open(clients_path, "w")
		json.dump(clients_json, fd)
		fd.close()
		return

	"""
	Permet de supprimer un client de la base
	"""
	def delete_client(self, client_id:int) -> None:
		self.dict_clients.pop(client_id)

		#On charge les données des clients stockées dans le fichier Clients.json
		fd = open(clients_path, "r")
		clients_json = json.load(fd)
		fd.close()

		#On supprime le client dans le fichier Clients.json puis on sauvegarde
		clients_json.pop(str(client_id))
		fd = open(clients_path, "w")
		json.dump(clients_json, fd)
		fd.close()

		self.update_newClient_id()
		return

	def search_client(self, search_value:str) -> list:
		res = []

		if self.search_filter_index == 0:
			res = search_by_name(self.dict_clients, search_value)
		elif self.search_filter_index == 1:
			res = search_by_address(self.dict_clients, search_value)
		elif self.search_filter_index == 2:
			res = search_by_tel(self.dict_clients, search_value)

		return res

	def change_search_filter(self, new_search_filter_index:int) -> None:
		self.search_filter_index = new_search_filter_index
		return
client_mng = Client_mng()
