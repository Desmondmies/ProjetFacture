class Client:
    def __init__(self, nom, prenom, tel, mail, adresse, description = None, liste_factures = None):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.mail = mail
        self.adresse = adresse
        self.description = description

        self.liste_factures = liste_factures
        self.liste_devis = liste_devis
    
