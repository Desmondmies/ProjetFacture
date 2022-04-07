class Facture:
    def __init__(self, num: int, client, deadline, liste_produits:list = None) -> None:
        self.num = num
        self.client = client
        #self.date_creation = date_actuelle #CHECKER : date_echeance > date_creation
        self.deadline = deadline

        self.liste_produits = liste_produits
