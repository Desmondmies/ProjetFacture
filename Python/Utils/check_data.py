from datetime import datetime, date

"""
Contrôle que les données de la factures sont valides (il faut que toutes les données soient renseignées)
"""
def check_invoice(dict_data_invoice:dict) -> list:
    creation_date = datetime.strptime(dict_data_invoice["creation_date"], '%Y-%m-%d').date()
    due_date = datetime.strptime(dict_data_invoice["due_date"], '%Y-%m-%d').date()

    errors = []

    #Contrôle des dates
    if  creation_date < date.today() or creation_date > due_date:
        errors.append("creation_date")
        errors.append("due_date")

    #Au moins un produit inscrit sur la facture
    if dict_data_invoice["list_items"].count("") != len(dict_data_invoice["list_items"]):
        errors.append("list_items")
    
    #Contrôle des dates des acomptes
    for deposit_id in range(len(dict_data_invoice["list_deposits"])):
        payment_date = datetime.strptime(dict_data_invoice["list_deposits"][deposit_id]["payment_date"], '%Y-%m-%d').date() 
        if payment_date < creation_date:
            errors.append("list_deposits")
            break
    
    return errors

def check_estimate(dict_data_estimate:dict) -> list:
    creation_date = datetime.strptime(dict_data_estimate["creation_date"], '%Y-%m-%d').date()
    due_date = datetime.strptime(dict_data_estimate["due_date"], '%Y-%m-%d').date()

    errors = []

    #Contrôle des dates
    if  creation_date < date.today():
        errors.append("creation_date")

    #Au moins un produit inscrit sur le devis
    if dict_data_estimate["list_items"].count("") != len(dict_data_estimate["list_items"]):
        errors.append("list_items")
    
    return errors