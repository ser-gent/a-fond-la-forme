from .Epreuve import Epreuve
import math

class Saut(Epreuve):
    def __init__(self, saut, mesure,genre):
        super(Saut,self).__init__(saut, "cm")
        self.nom = saut
        self.perf = self.conversion(mesure)
        self.score = self.calculerPoint(genre)

    # Convertir de m en cm
    def conversion(self, mesure):
        return round(mesure*100, 2)

    # Calcul des points
    def calculerPoint(self,genre):
        if (genre == 1) :
            SautIndex = {
                #              a     b     c
                "Hauteur":  (0.8465, 75.0, 1.42),
                "Perche":   (0.2797, 100.0, 1.35),
                "Longueur": (0.14354, 220.0, 1.40),
            }

        else :
            SautIndex = {
                   #              a     b     c
                "Hauteur":  (1.84523, 75.0, 1.348),
                "Longueur": (0.188807, 210.0, 1.41),
            }


        (a, b, c) = SautIndex.get(self.nom)
        P = a*(self.perf - b)**c
        
        return math.floor(P)
        
    def details(self):
        print("----------------")
        print("Type de saut : " + self.nom)
        if(self.nom == "Longueur"):
          print("Vent = " + str(self.vent))

        print("Performance réalisée : " + str(self.perf) + " " + self.unite+ " - " + str(self.score) + " points")