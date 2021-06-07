class Participant:
    def __init__(self, nom, prenom, genre, nationalite):
        self.nom = nom
        self.prenom = prenom
        self.genre = genre
        self.nationalite = nationalite

    def details(self):
        print(self.nom)
        print(self.prenom)
        print(self.genre)
        print(self.nationalite)
