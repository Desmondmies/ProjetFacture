class Client:
    """
    def __init__(self, id_client:int, surname:str, firstname:str, phone:str, mail:str, adress:str, postcode:int, description:str = None, list_invoices:list = None, list_estimates:list = None) -> None:
        self.data = {}
        self.data["id"] = id_client #numéro client correspondant aussi à son nom de fichier
        self.data["surname"] = surname
        self.data["firstname"] = firstname
        self.data["phone"] = phone
        self.data["mail"] = mail
        self.data["adress"] = adress
        self.data["postcode"] = postcode
        self.data["description"] = description

        self.data["list_invoices"] = list_invoices
        self.data["list_estimates"] = list_estimates
    """
    def __init__(self, dict_data_client:dict) -> None:
        self.data = dict_data_client
        return

    def __getitem__(self, key):
        # print("getter method called CLIENT")
        if key == "all":
            return self.data
        if key not in self.data.keys():
            return None
        return self.data[key]

    def __setitem__(self, key, value) -> bool:
        # print("mutateur !")
        if key not in self.data.keys():
            return False
        self.data[key] = value
        return True
