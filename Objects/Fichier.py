import os
import pickle


class Fichier:
    def __init__(self, storage_path):
        """
        Constructeur

        Args:
            storage_path (string): chemin absolu du fichier de stockage de sauvegarde
        """
        self.storage_path = storage_path

    def sauvegarder(self, objet_a_sauvegarder, nom_fichier):
        """
        Sauvegarde les fichiers dans le répertoire de sauvegarde

        Args:
            objet_a_sauvegarder (*): Objet à sauvegarder
            nom_fichier (string): nom à donner au fichier de sauvegarde
        """
        os.chdir(self.storage_path)
        with open(nom_fichier, "wb") as file:
            pickle.dump(objet_a_sauvegarder, file)

    def charger(self, nom_fichier):
        """
        Charge l'objet d'un fichier

        Args:
            nom_fichier (string): nom du fichier

        Returns:
            *: [description]
        """
        os.chdir(self.storage_path)
        with open(nom_fichier, "rb") as file:
            object_charge = pickle.load(file)
        return object_charge

    def explorer(self):
        """
        Explore le dossier de stockage

        Returns:
            list: liste des fichier du répertoire
        """
        liste_fichier = []
        for path, dirs, files in os.walk(self.storage_path):
            for filename in files:
                liste_fichier.append(filename)
        return liste_fichier
