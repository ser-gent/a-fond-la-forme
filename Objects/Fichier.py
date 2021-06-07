import os
import pickle


class Fichier:
    def __init__(self, storage_path):
        self.storage_path = storage_path

    def sauvegarder(self, objet_a_sauvegarder, nom_fichier):
        os.chdir(self.storage_path)
        with open(nom_fichier, "wb") as file:
            pickle.dump(objet_a_sauvegarder, file)

    def charger(self, nom_fichier):
        os.chdir(self.storage_path)
        with open(nom_fichier, "rb") as file:
            object_charge = pickle.load(file)
        return object_charge

    def explorer(self):
        liste_fichier = []
        for path, dirs, files in os.walk(self.storage_path):
            for filename in files:
                liste_fichier.append(filename)
        return liste_fichier
