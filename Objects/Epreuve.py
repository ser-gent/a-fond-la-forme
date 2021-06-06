class Epreuve:
    """
    Classe mère représentant les épreuves des combinées
    """
    def __init__(self, nom, unite) -> None:
        """
        Constructeur

        Args:
            nom (str): nom de l'épreuve
            unite (int): unite de la performance
        """
        self.nom = nom
        self.unite = unite

    def __str__(self) -> str:
        """
        Détails de l'épreuve

        Returns:
            str: détails de l'épreuve
        """
        return self.nom+"("+self.unite+")"
