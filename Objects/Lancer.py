import math
from .Epreuve import Epreuve

class Lancer(Epreuve):

    # Constructeur
    def __init__(self, nom, mesure, genre) -> None:
        #super(Lancer, self).__init__(nom, "m")
        super().__init__(nom, "m")
        self.perf = float(mesure)
        self.score = self.calculer_points(genre)


    # Calcul des points
    def calculer_points(self, genre):
        if genre == 1 :
            index_lancer = {
                #              a    b      c
                "Javelot":  (10.14, 7.00, 1.08),
                "Disque":   (12.91, 4.00, 1.10),
                "Poids":    (51.39, 1.50, 1.05),
            }


        else :
            index_lancer = {
                #              a    b      c
                "Javelot":  (15.9803, 3.80, 1.04),
                "Poids":    (56.0211, 1.50, 1.05),
            }


        (a, b, c) = index_lancer.get(self.nom)
        P = a*(self.perf - b)**c
        return math.floor(P)

    # Affiche les détails de l'épreuve
    def details(self) -> None:
        print(self.nom+ " -> "
            + str(self.perf)+ " " + self.unite + " - " + str(self.score) + " points")
        print("----------------")
