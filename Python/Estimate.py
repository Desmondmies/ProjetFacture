class Estimate:
    """
    def __init__(self, num:int, creation_date:str, client:Client, list_items:list = None) -> None:
        self.data = {}
        self.data["id"] = num
        self.data["creation_date"] = creation_date
        self.data["client_id"] = client

        self.data["artisan"] = dict_data_artisan

        self.data["list_items"] = list_items

        return
    """

    def __init__(self, dict_data_estimate:dict) -> None:
        self.data = dict_data_estimate
        return

    def __getitem__(self, key):
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

    #On considère une TVA de 20%
    def calculate_before_taxes(self) -> int:
        price = 0
        for item in self["list_items"] :
            price += item.calculate_cost()
            price -= 0.2 * price
        return price

    def calculate_taxes_included(self) -> int:
        price = 0
        for item in self["list_items"] :
            price += item.calculate_cost()
        return price
