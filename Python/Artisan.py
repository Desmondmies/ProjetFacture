class Artisan:
    def __init__(self, nom_ent, nom, prenom , tel, mail_ent, adresse_ent, logo = None, style = "STYLE2"):
        self.nom_ent = nom_ent
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.mail_comp = mail_ent
        self.adresse_ent = adresse_ent

        self.logo = logo
        #self.num_SIREN ou un truc du genre ?
        self.style_prefere = style
