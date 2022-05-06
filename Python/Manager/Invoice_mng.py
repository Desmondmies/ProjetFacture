import os
import json
from datetime import datetime

from Python.Invoice import Invoice
from Python.Utils.SearchData import search_by_name, search_by_address, search_by_tel

invoices_path = os.path.abspath("./JSON/Invoices.json")

class Invoice_mng:
    def __init__(self) -> None:
        self.dict_invoices = {} #Les numéros facture sont les clés et les valeurs sont un dictionnaire contenant les données de la facture choisi
        self.init_dict_invoices()

        self.update_newInvoice_id()

        self.search_filter_index = 0
        return

    """
    Initialisation du dictionnaire des factures présents dans le fichier "./JSON/Invoices.json".
    On charge le fichier en question puis on convertit chaque données des factures en instance de Invoice que l'on stocke dans le dictionnaire des factures.
    """
    def init_dict_invoices(self) -> None:
            fd = open(invoices_path, "r")
            dict_data_invoices = json.load(fd)
            fd.close()

            for invoice_id, dict_data_invoice in dict_data_invoices.items():
                self.dict_invoices[int(invoice_id)] = Invoice(dict_data_invoice)
            return

    def update_newInvoice_id(self) -> None:
        if len(self.dict_invoices) == 0:
            self.newInvoice_id = 0
        else:
            self.newInvoice_id = max(self.dict_invoices) + 1 #Numéro de la prochaine facture à créer : pas en fonction du nombre de factures car un dictionnaire de mille factures ne signifie pas que la dernière facture a le numéro 1000

    """
    On créé une instance de Invoice puis on met à jour le dictionnaire des factures existantes, le fichier json et le numéro de la prochaine facture
    """
    def create_invoice(self, dict_data_invoice:dict) -> None:
        """
        On contrôle les données de la facture : date creation < due date ET au moins 1 item dans list_items
        """
        creation_date = datetime.strptime(dict_data_invoice["creation_date"], '%Y-%m-%d').date()
        due_date = datetime.strptime(dict_data_invoice["due_date"], '%Y-%m-%d').date()

        if creation_date > due_date:
            return
        if len(dict_data_invoice["list_items"]) < 1:
            return

        """
        On créé la facture
        """
        dict_data_invoice["id"] = self.newInvoice_id #On rajoute le numéro de la nouvelle facture
        #dict_data_invoice["artisan"] = Artisan.read_artisan() #IL FAUT QUE CE FICHIER AIT ACCES AUX DONNEES DE L'ARTISAN
        self.dict_invoices[self.newInvoice_id] = Invoice(dict_data_invoice)

        #On charge les données des factures stockées dans le fichier Invoices.json
        fd = open(invoices_path, "r")
        invoices_json = json.load(fd)
        fd.close()

        #On rajoute les données de la facture dans le fichier Invoices.json puis on sauvegarde
        invoices_json[str(self.newInvoice_id)] = dict_data_invoice
        fd = open(invoices_path, "w")
        json.dump(invoices_json, fd)
        fd.close()

        self.newInvoice_id += 1

        return

    """
    Renvoie toutes les données concernant une facture
    """
    def read_invoice(self, invoice_id:int) -> Invoice:
        #print(self.dict_invoices[invoice_id]["all"]) ON AFFICHE OU ON RENVOIE LES DONNEES DU CLIENT ?
        return self.dict_invoices[invoice_id]["all"] #"all" est un mot clé créer pour récupérer les données d'une facture

    """
    Permet de modifier les informations d'une facture stockée grâce à son numéro de facture, le nom de l'attribut et de la nouvelle valeur
    """
    def update_invoice(self, invoice_id:int, attribute:str, new_val) -> None:
        self.dict_invoices[invoice_id][attribute] = new_val

        #On charge les données des facture stockées dans le fichier Invoices.json
        fd = open(invoices_path, "r")
        invoices_json = json.load(fd)
        fd.close()

        #On modifie les données de la facture dans le fichier Invoices.json puis on sauvegarde
        invoices_json[str(invoice_id)][attribute] = new_val
        fd = open(invoices_path, "w")
        json.dump(invoices_json, fd)
        fd.close()
        return

    """
    Permet de supprimer une facture de la base. Il faut que "invoice_id" fasse référence à une facture existante
    """
    def delete_invoice(self, invoice_id:int) -> None:
        self.dict_invoices.pop(invoice_id)

        #On charge les données des factures stockées dans le fichier Invoices.json
        fd = open(invoices_path, "r")
        invoices_json = json.load(fd)
        fd.close()

        #On supprime la facture dans le fichier Invoices.json puis on sauvegarde
        invoices_json.pop(str(invoice_id))
        fd = open(invoices_path, "w")
        json.dump(invoices_json, fd)
        fd.close()

        self.update_newInvoice_id()
        return

    def search_client(self, search_value:str) -> dict:
        res = {}

        if self.search_filter_index == 0:
            res = search_by_name(self.dict_invoices, search_value)
        elif self.search_filter_index == 1:
            res = search_by_address(self.dict_invoices, search_value)
        elif self.search_filter_index == 2:
            res = search_by_tel(self.dict_invoices, search_value)

        return res

    def change_search_filter(self, new_search_filter_index:int) -> None:
        self.search_filter_index = new_search_filter_index

invoice_mng = Invoice_mng()