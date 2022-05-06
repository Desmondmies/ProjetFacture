import os
import json

artisan_path = os.path.abspath("./JSON/Artisan.json")

class Artisan:
    def __init__(self) -> None:
        self.data = {}
        self.artisan_is_set = False

        self.load_artisan()
        self.test_datas_set()

    def load_artisan(self) -> None:
        fd = open(artisan_path, "r")
        self.data = json.load(fd)
        fd.close()

    """
    Cette fonction vérifie que toutes les données de l'artisan sont initialisées et modifie la  variable "artisan_is_set" en fonction
    """
    def test_datas_set(self) -> None:
        self.artisan_is_set = not "" in self.data.values()

    def __getitem__(self, key):
        if key == "all":
            return self.data
        if key not in self.data.keys():
            return None
        return self.data[key]

    def __setitem__(self, key, value) -> bool:
        if key not in self.data.keys():
            return False
        self.data[key] = value
        self.test_datas_set() #A chaque fois qu'une donnée est modifiée, on contrôle si toutes les données sont renseignées

        #On modifie les données de l'artisan dans le fichier Artisan.json puis on sauvegarde
        fd = open(artisan_path, "w+")
        #json.dump(artisan_json, fd)
        json.dump(self.data, fd)
        fd.close()
        return True

    def read_artisan(self) -> dict:
        return self["all"]

    def isArtisanComplete(self) -> bool:
        return self.artisan_is_set

artisan = Artisan()
