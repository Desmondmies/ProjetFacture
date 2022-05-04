class Devis:
    def __init__(self, num, client, liste_produits = None):
        self.num = num
        self.client = client
        
        self.liste_produits = liste_produits

        self.solde_total = 0 #A calculer