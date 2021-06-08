from Objects.Lancer import Lancer
from Objects.Course import Course
from Objects.Saut import Saut
from prettytable import PrettyTable


class Decathlon:
    def __init__(self, perfs, athlete) -> None:
        """
        Constructeur

        Args:
            perfs (tuple): performance de l'ahlète
            athlete (Participant): athlète
        """
        self.perfs = (
            Course(100, perfs[0], False, 1),
            Saut("Longueur", perfs[1], 1),
            Lancer("Poids", perfs[2], 1),
            Saut("Hauteur", perfs[3], 1),
            Course(400, perfs[4], False, 1),
            Course(110, perfs[5], True, 1),
            Lancer("Disque", perfs[6], 1),
            Saut("Perche", perfs[7], 1),
            Lancer("Javelot", perfs[8], 1),
            Course(1500, perfs[9], False, 1),
        )
        self.athlete = athlete
        self.score_total = self.total()

    def total(self):
        """
        Calcul le total des épreuves du décathlon

        Returns:
            int: total du décathlon
        """
        total = 0
        for e in range(len(self.perfs)):
            total = total + self.perfs[e].score
        return total

    def details(self) -> None:
        """
        Affiche les détails di décathlon
        """
        print("--- Recap ---")
        print("NOM : " + self.athlete.prenom + " " + self.athlete.nom)
        resultats = PrettyTable()
        resultats.field_names = ["Epreuve", "Performance", "Score"]
        for i in range(len(self.perfs)):
            resultats.add_row(
                [
                    self.perfs[i].nom,
                    (str(self.perfs[i].perf) + "" + self.perfs[i].unite),
                    self.perfs[i].score,
                ]
            )
        print(resultats)
        print("TOTAL : " + str(self.score_total) + " points")
