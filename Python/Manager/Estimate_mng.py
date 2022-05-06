import os
import json

from Python.Manager.Artisan import artisan

from Python.Estimate import Estimate
from Python.Utils.SearchData import search_by_name, search_by_address, search_by_tel


estimate_path = os.path.abspath("./JSON/Estimates.json")

class Estimate_mng:
    def __init__(self) -> None:
        self.dict_estimates = {} #Les numéros des devis sont les clés et les valeurs sont une instance de Estimate 
        self.init_dict_estimate()

        self.update_newEstimate_id()

        self.search_filter_index = 0
        return

    """
    Initialisation du dictionnaire des devis présents dans le fichier "./JSON/Estimate.json".
    On charge le fichier en question puis on convertit chaque données des devis en instance de Estimate que l'on stocke dans le dictionnaire des devis.
    """

    def init_dict_estimate(self) -> None:
            fd = open(estimate_path, "r")
            dict_estimate = json.load(fd)
            fd.close()

            for estimate_id, dict_estimate in dict_estimate.items():
                self.dict_estimates[int(estimate_id)] = Estimate(dict_estimate)
            return

    def update_newEstimate_id(self) -> None:
        if len(self.dict_estimates) == 0:
            self.newEstimate_id = 0
        else:
            self.newEstimate_id = max(self.dict_estimates) + 1 #Numéro du prochain devis à créer : pas en fonction du nombre de devis car un dictionnaire de mille devis ne signifie pas que le dernier devis a le numéro 1000

    """
    On créé une instance de devis puis on met à jour le dictionnaire des devis existantes, le fichier json et le numéro de la prochaine devis
    """
    def create_estimate(self, dict_data_estimate:dict) -> None:
        """
        On contrôle les données du devis : au moins 1 item dans list_items
        
        if len(dict_data_invoice["list_items"]) < 1:
            return
        """
        """
        On créé la facture
        """
        dict_data_estimate["id"] = self.newEstimate_id #On rajoute le numéro du nouveau devis
        dict_data_estimate["artisan"] = artisan.read_artisan() #IL FAUT QUE CE FICHIER AIT ACCES AUX DONNEES DE L'ARTISAN
        self.dict_estimates[self.newEstimate_id] = Estimate(dict_data_estimate)

        #On charge les données des devis stockées dans le fichier Estimates.json
        fd = open(estimate_path, "r")
        estimate_json = json.load(fd)
        fd.close()

        #On rajoute les données du devis dans le fichier Estimate.json puis on sauvegarde
        estimate_json[str(self.newEstimate_id)] = dict_data_estimate
        fd = open(estimate_path, "w")
        json.dump(estimate_json, fd)
        fd.close()

        self.newEstimate_id += 1
        return

    """
    Renvoie toutes les données concernant un devis
    """
    def read_estimate(self, estimate_id:int) -> Estimate:
        return self.dict_estimates[estimate_id]["all"] #"all" est un mot clé créé pour récupérer les données d'un devis

    """
    Permet de modifier les informations d'un devis stocké grâce à son numéro, le nom de l'attribut et de la nouvelle valeur
    """
    def update_estimate(self, estimate_id:int, attribute:str, new_val) -> None:
        self.dict_estimates[estimate_id][attribute] = new_val

        #On charge les données des devis stockées dans le fichier Estimates.json
        fd = open(estimate_path, "r")
        estimate_json = json.load(fd)
        fd.close()

        #On modifie les données du devis dans le fichier Estimates.json puis on sauvegarde
        estimate_json[str(estimate_id)][attribute] = new_val
        fd = open(estimate_path, "w")
        json.dump(estimate_json, fd)
        fd.close()
        return

    """
    Permet de supprimer un devis de la base. Il faut que "estimate_id" fasse référence à un devis existant
    """
    def delete_estimate(self, estimate_id:int) -> None:
        self.dict_estimates.pop(estimate_id)

        #On charge les données des devis stockées dans le fichier Estimate.json
        fd = open(estimate_path, "r")
        estimate_json = json.load(fd)
        fd.close()

        #On supprime le devis dans le fichier Estimates.json puis on sauvegarde
        estimate_json.pop(str(estimate_id))
        fd = open(estimate_path, "w")
        json.dump(estimate_json, fd)
        fd.close()

        self.update_newEstimate_id()
        return

    def search_client(self, search_value:str) -> list:
        res = []

        if self.search_filter_index == 0:
            res = search_by_name(self.dict_estimates, search_value)
        elif self.search_filter_index == 1:
            res = search_by_address(self.dict_estimates, search_value)
        elif self.search_filter_index == 2:
            res = search_by_tel(self.dict_estimates, search_value)

        return res

    def change_search_filter(self, new_search_filter_index:int) -> None:
        self.search_filter_index = new_search_filter_index
        return

estimate_mng = Estimate_mng()