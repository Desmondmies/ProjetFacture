class Invoice:
    """
    #Le numéro d'une facture est unique et est géré par le "invoice manager"
    def __init__(self, invoice_id:int, client_id:int, creation_date:str, due_date:str, acquitted:bool, comment:str, list_items:list = None, list_deposits:list = None) -> None:
        self.data = {}
        self.data["invoice_id"] = invoice_id
        self.data["client_id"] = client_id
        self.data["creation_date"] = creation_date
        self.data["due_date"] = due_date
        self.data["comment"] = comment
        self.data["acquitted"] = acquitted

        self.data["artisan"] = dico_data_artisan

        self.data["list_items"] = list_items
        self.data["list_deposits"] = list_deposits
        return
    """
    def __init__(self, dict_data_invoice:dict) -> None:
        self.data = dict_data_invoice
        return

    def __getitem__(self, key):
        if key == "all":
            return self.data
        if key not in self.data.keys():
            return None
        return self.data[key]

    def __setitem__(self, key, value) -> bool:
        if key not in self.data.keys():
            return False
        self.data[key] = value
        return True