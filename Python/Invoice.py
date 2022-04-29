from Python.Client import Client

class Invoice:
    #Le numéro d'une facture est unique et est géré par le "invoice manager"
    def __init__(self, num:int, client:Client, creation_date:str, due_date:str, acquitted:bool, comment:str, list_items:list = None, list_deposits:list = None) -> None:
        self.data = {}
        self.data["num"] = num #Doit valoir numMax existant + 1
        self.data["client"] = client
        self.data["creation_date"] = creation_date
        self.data["due_date"] = due_date
        self.data["comment"] = comment
        self.data["acquitted"] = acquitted

        self.data["list_items"] = list_items
        self.data["list_deposits"] = list_deposits
        ###############MANQUE DONNEES DE L'ARTISAN
        return

    def __getitem__(self, key):
        print("getter method called")
        if key not in self.data.keys():
            return None
        return self.data[key]

    def __setitem__(self, key, value) -> bool:
        print("mutateur !")
        if key not in self.data.keys():
            return False
        self.data[key] = value
        return True
