class Deposit:
    def __init__(self, amount:int, payment_date:str) -> None:
        self.data = {}
        self.data["amount"] = amount
        self.data["payment_date"] = payment_date
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
