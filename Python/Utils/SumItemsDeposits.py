def get_total_deposits(dico) -> int:
    sum = 0
    for depo in dico["list_deposits"]:
        if "amount" not in depo.keys(): continue
        sum += depo["amount"]
    return sum

def get_total_price(dico) -> int:
    sum = 0
    for it in dico["list_items"]:
        if "quantity" not in it.keys(): continue
        if "price" not in it.keys(): continue
        sum += (it["quantity"] * it["price"])
    return sum

def IsTotalPaid(dico) -> bool:
    return get_total_deposits(dico) >= get_total_price(dico)