class Participant:
    def __init__(self, nom, prenom, genre, nationalite):
        """
        Constructeur

        Args:
            nom (string): nom de l'ahlète
            prenom (string): prénom de l'athlète
            genre (integer): 0 si femme, 1 si homme
            nationalite (string): Code olympique du pays de l'athlète (https://fr.wikipedia.org/wiki/Liste_des_codes_pays_du_CIO)
        """
        self.nom = nom
        self.prenom = prenom
        self.genre = genre
        self.nationalite = nationalite

    def details(self):
        """
        Affiche les détails de l'athlète
        """
        print(self.nom)
        print(self.prenom)
        print(self.genre)
        print(self.nationalite)
