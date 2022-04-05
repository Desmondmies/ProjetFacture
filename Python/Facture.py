class Facture:
    def __init__(self, num, client, date_echeance, liste_produits = None):
        self.num = num
        self.client = client
        #self.date_creation = date_actuelle #CHECKER : date_echeance > date_creation
        self.date_echeance = date_echeance
        
        self.liste_produits = liste_produits