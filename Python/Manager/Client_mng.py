import os
import json
import glob

from Python.Client import Client

clients_path = os.path.abspath("./JSON/Client")

class Client_mng:
    def __init__(self) -> None:
        self.list_clients = [] #Les numéros client vont du numéro le plus élévé (à l'indice 0) vers le plus bas (à l'indice n)  
        self.init_list_clients()

        self.client_id = self.list_clients[0]["id"] + 1 #Numéro du prochain client à créer

        return

    """
    Initialisation de la liste des clients existants dans le dossier "./JSON/Client"
    """
    def init_list_clients(self) -> None:
        list_client_file = glob.glob(clients_path + "/*.json")
        #Pour chaque fichier client dans le dossier JSON/Client
        for file_name in list_client_file:
            fd = open(file_name, "r")
            dict_data_client = json.load(fd)
            fd.close()
            client = Client(dict_data_client)
            self.list_clients = [client] + self.list_clients
    
    def create_client(self, dict_data_client) -> None:
        client = Client(dict_data_client)
        #On créé un fichier json associé au client dont le nom correspond à : numéro_client.json
        fd = open(str(self.client_id) + ".json", "w")
        json.dump(dict_data_client, fd)
        fd.close()
        self.client_id += 1
        self.list_clients = [client] + self.list_clients
        return
    
    def read_client(self, client_id) -> None:
        return

    """
    Permet de modifier les informations d'un client à partir du nom de l'attribut et de sa nouvelle valeur 
    """
    def update_client(self, key, value) -> None:
        
        return

    def delete_client(self) -> None:
        return