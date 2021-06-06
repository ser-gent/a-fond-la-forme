from Objects.Lancer import Lancer
from Objects.Course import Course
from Objects.Saut import Saut
from prettytable import PrettyTable

class Heptathlon:
    def __init__(self, perfs, athlete):
        self.perfs = (
            Course(100, perfs[0], True, 0),
            Saut("Hauteur", perfs[1], 0),
            Lancer("Poids", perfs[2], 0),
            Course(200, perfs[3],False, 0),
            Saut("Longueur", perfs[4], 0),
            Lancer("Javelot", perfs[5],0),
            Course(800, perfs[6], False, 0),
        )
        self.athlete = athlete
        self.score_total = self.total()

    def total(self):
        total = 0
        for epreuve in range(len(self.perfs)):
            total = total + self.perfs[epreuve].score
        return total
   
    def details(self) -> None:
        print("--- Recap ---")
        print("NOM : " +self.athlete.prenom+ " " +self.athlete.nom)
        resultats = PrettyTable()
        resultats.field_names = ["Epreuve", "Performance", "Score"]
        for index in range(len(self.perfs)):
            resultats.add_row([self.perfs[index].nom, (str(self.perfs[index].perf)+""+self.perfs[index].unite), self.perfs[index].score])
        print(resultats)
        print("TOTAL : " +str(self.score_total)+ " points")
