class Item:
    def __init__(self, name:str, description:str, quantity:int, price:int) -> None:
        self.data = {}
        self.data["name"] = name
        self.data["description"] = description
        self.data["quantity"] = quantity
        self.data["price"] = price

    def __getitem__(self, key):
        # print("getter method called")
        if key not in self.data.keys():
            return None
        return self.data[key]

    def __setitem__(self, key, value) -> bool:
        # print("mutateur !")
        if key not in self.data.keys():
            return False
        self.data[key] = value
        return True

    def calculate_cost(self) -> int:
        return self["price"] * self["quantity"]
