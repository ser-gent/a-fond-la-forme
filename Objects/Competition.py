from prettytable import PrettyTable


class Competition:
    def __init__(self, nom, lieu) -> None:
        """
        Constructeur

        Args:
            nom (string): Nom de la compétition
            lieu (string): Lieu de la compétition
        """
        self.nom = nom
        self.lieu = lieu
        self.combined_event = []

    def add_participation(self, combined_event) -> None:
        """
        Ajouter les décathlon/heptathlon d'un participant à la compétition

        Args:
            combined_event (Decathlon | Heptathlon): Epreuves combinées d'un athlète
        """
        self.combined_event.append(combined_event)
        self.classer()

    def classer(self) -> None:
        """
        Classer les participants dans l'ordre (total le plus grand en premier)
        """
        self.combined_event.sort(key=lambda ce: ce.score_total, reverse=True)

    def recap(self) -> None:
        """
        Affiche le récapitulatif de la compétition
        """
        print("")
        print("COMPETITION : " + self.nom)
        if len(self.combined_event) > 0:
            recap = PrettyTable()
            headers = []
            headers.append("Clt")
            headers.append("Athlète")
            headers.append("Nation")
            for index in range(len(self.combined_event[0].perfs)):
                headers.append(self.combined_event[0].perfs[index].nom)
            headers.append("Total")
            recap.field_names = headers
            for event in range(len(self.combined_event)):
                ligne_resultats = []
                for epreuve_decathlon in range(len(self.combined_event[event].perfs)):
                    ligne_resultats.append(
                        str(self.combined_event[event].perfs[epreuve_decathlon].perf)
                    )
                    # +" ("+str(self.combined_event[d].perfs[e].score)+ ")")
                ligne_resultats.append(self.combined_event[event].score_total)
                recap.add_row(
                    [
                        str(event + 1),
                        self.combined_event[event].athlete.prenom
                        + " "
                        + self.combined_event[event].athlete.nom,
                        self.combined_event[event].athlete.nationalite,
                    ]
                    + ligne_resultats
                )

        else:
            recap = "Pas de données"
        print(recap)
