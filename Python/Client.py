class Client:
    def __init__(self, surname, name, phone, mail, adress, description = None, list_invoices = None, list_estimates = None):
        self.data = {}
        self.data["surname"] = surname
        self.data["name"] = name
        self.data["phone"] = phone
        self.data["mail"] = mail
        self.data["adress"] = adress
        self.data["description"] = description

        self.data["list_invoices"] = list_invoices
        self.data["list_estimates"] = list_estimates

    def __getitem__(self, key):
        print("getter method called")
        if key not in self.data.keys():
            return None
        return dict_info[key]

    def __setitem__(self, key, value):
        if key not in self.data.keys():
            return False
        self.data[key] = value
        return True
