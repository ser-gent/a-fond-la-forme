from Objects.Competition import Competition
from Objects.Decathlon import Decathlon
from Objects.Participant import Participant

p_mayer = (
    10.55,  # 100m
    7.80,  # Longueur
    16.00,  # Poids
    2.05,  # Hauteur
    48.42,  # 400m
    13.75,  # 110m Haies
    50.54,  # Disque
    5.45,  # Perche
    71.90,  # Javelot
    276.11,  # 1500 m
)

p_abele = (
    10.84,  # 100m
    7.19,  # Longueur
    15.20,  # Poids
    1.93,  # Hauteur
    48.48,  # 400m
    13.86,  # 110m Haies
    44.67,  # Disque
    4.75,  # Perche
    65.35,  # Javelot
    273.78,  # 1500 m
)

p_nowak = (
    11.19,  # 100m
    7.56,  # Longueur
    14.50,  # Poids
    1.96,  # Hauteur
    49.29,  # 400m
    14.72,  # 110m Haies
    45.31,  # Disque
    4.85,  # Perche
    64.00,  # Javelot
    266.80,  # 1500 m
)

deca_tn = Decathlon(p_nowak, Participant("Nowak", "Tim", 1, "GER"))
deca_aa = Decathlon(p_abele, Participant("Abele", "Arthur", 1, "GER"))
deca_km = Decathlon(p_mayer, Participant("Mayer", "Kévin", 1, "FRA"))

decastart = Competition("Décastart", "Talence")
decastart.add_participation(deca_tn)
decastart.add_participation(deca_km)
decastart.add_participation(deca_aa)
decastart.recap()
