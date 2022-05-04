class Artisan:
    def __init__(self, nom_ent, tel, mail_ent, adresse_ent, logo = None, style = "STYLE2"):
        self.nom_ent = nom_ent
        self.tel = tel
        self.mail_ent = mail_ent
        self.adresse_ent = adresse_ent

        self.logo = logo
        #self.num_SIREN ou un truc du genre ?
		self.style_prefere = style
