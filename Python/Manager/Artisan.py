import os
import json

artisan_path = os.path.abspath("./JSON/Artisan.json")

class Artisan:
    def __init__(self) -> None:
        self.data = {}
        self.artisan_is_set = False

        self.load_artisan()
        self.test_datas_set()
        return

    def load_artisan(self) -> None:
        fd = open(artisan_path, "r")
        self.data = json.load(fd)
        fd.close()
        #self.num_SIREN ?
        return

    """
    Cette fonction vérifie que toutes les données de l'artisan sont initialisées et modifie la  variable "artisan_is_set" en fonction
    """
    def test_datas_set(self) -> None:
        self.artisan_is_set = not "" in self.data.values()
        return 

    def __getitem__(self, key):
        if key not in self.data.keys():
            return None
        return self.data[key]

    def __setitem__(self, key, value) -> bool:
        if key not in self.data.keys():
            return False
        self.data[key] = value
        self.test_datas_set() #A chaque fois qu'une donnée est modifiée, on contrôle si toutes les données sont renseignées
        return True

#METTRE A JOUR ARTISAN.JSON QUAND ON MODIFIE LES DONNEES DE L'ARTISAN