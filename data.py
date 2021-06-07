import os
from Objects.Fichier import Fichier
from Objects.Competition import Competition
from Objects.Decathlon import Decathlon
from Objects.Participant import Participant
from Objects.Heptathlon import Heptathlon



p_mayer = (
    10.55,          # 100m
    7.80,            # Longueur
    16.00,          # Poids
    2.05,            # Hauteur
    48.42,          # 400m
    13.75,          # 110m Haies
    50.54,          # Disque
    5.45,            # Perche
    71.90,          # Javelot
    276.11          # 1500 m
)

p_abele = (
    10.84,          # 100m
    7.19,            # Longueur
    15.20,          # Poids
    1.93,            # Hauteur
    48.48,          # 400m
    13.86,          # 110m Haies
    44.67,          # Disque
    4.75,            # Perche
    65.35,          # Javelot
    273.78          # 1500 m
)

p_nowak = (
    11.19,          # 100m
    7.56,            # Longueur
    14.50,          # Poids
    1.96,            # Hauteur
    49.29,          # 400m
    14.72,          # 110m Haies
    45.31,          # Disque
    4.85,            # Perche
    64.00,          # Javelot
    266.80          # 1500 m
)

p_braun = (
    11.17,          # 100m
    7.29,            # Longueur
    14.37,          # Poids
    2.02,            # Hauteur
    49.09,          # 400m
    14.61,          # 110m Haies
    46.51,          # Disque
    4.45,            # Perche
    56.51,          # Javelot
    276.39          # 1500 m
)

decastart = Competition("Décastart-Décathlon", "Talence")
decastart.add_participation(Decathlon(p_nowak, Participant("Nowak", "Tim", 1, "GER")))
decastart.add_participation(Decathlon(p_mayer, Participant("Mayer", "Kévin", 1, "FRA")))
decastart.add_participation(Decathlon(p_abele, Participant("Abele", "Arthur", 1, "GER")))
decastart.add_participation(Decathlon(p_braun, Participant("Braun", "Pieter", 1, "NED")))
save = Fichier(os.path.join(os.getcwd(), "storage"))
save.sauvegarder(decastart,decastart.nom)


p_thiam = (
    13.56,          # 100m Haies
    1.98,           # Hauteur
    14.91,          # Poids
    25.10,          # 200m
    6.58,           # Longueur
    53.13,          # Javelot
    136.54          # 800 m
)

p_ennis_hill = (
    12.84,          # 100m Haies
    1.89,           # Hauteur
    13.86,          # Poids
    23.49,          # 200m
    6.34,           # Longueur
    46.06,          # Javelot
    129.07          # 800 m
)

p_theisen_eaton = (
    13.18,          # 100m Haies
    1.86,           # Hauteur
    13.45,          # Poids
    24.18,          # 200m
    6.48,           # Longueur
    47.36,          # Javelot
    129.50          # 800 m
)

p_ikauniece = (
    13.33,          # 100m Haies
    1.77,           # Hauteur
    13.52,          # Poids
    23.76,          # 200m
    6.12,           # Longueur
    55.93,          # Javelot
    129.43          # 800 m
)

p_schafer = (
    13.12,          # 100m Haies
    1.83,           # Hauteur
    14.57,          # Poids
    23.99,          # 200m
    6.20,           # Longueur
    47.99,          # Javelot
    136.52          # 800 m
)

p_johnson_thompson = (
    13.48,          # 100m Haies
    1.98,           # Hauteur
    11.68,          # Poids
    23.26,          # 200m
    6.51,           # Longueur
    36.36,          # Javelot
    130.47          # 800 m
)

p_rodriguez = (
    13.61,          # 100m Haies
    1.86,           # Hauteur
    13.69,          # Poids
    24.26,          # 200m
    6.25,           # Longueur
    48.89,          # Javelot
    134.65          # 800 m
)

p_farkas = (
    13.79,          # 100m Haies
    1.86,           # Hauteur
    14.39,          # Poids
    25.38,          # 200m
    6.31,           # Longueur
    48.07,          # Javelot
    131.76          # 800 m
)

p_oeser = (
    13.69,          # 100m Haies
    1.86,           # Hauteur
    14.28,          # Poids
    24.99,          # 200m
    6.19,           # Longueur
    47.22,          # Javelot
    133.82          # 800 m
)

p_vetter = (
    13.47,          # 100m Haies
    1.77,           # Hauteur
    14.78,          # Poids
    23.93,          # 200m
    6.10,           # Longueur
    48.42,          # Javelot
    137.71          # 800 m
)

p_nana_djimou = (
    13.37,          # 100m Haies
    1.77,           # Hauteur
    14.88,          # Poids
    25.07,          # 200m
    6.43,           # Longueur
    48.76,          # Javelot
    140.36          # 800 m
)

hepta = Competition("Jeux Olympiques-Heptathlon", "Rio de Janeiro")
hepta.add_participation(Heptathlon(p_thiam, Participant("Thiam", "Nafissatou", 0, "BEL")))
hepta.add_participation(Heptathlon(p_ennis_hill, Participant("Ennis-Hill", "Jessica", 0, "GBR")))
hepta.add_participation(Heptathlon(p_theisen_eaton, Participant("Theisen-Eaton", "Brianne", 0, "CAN")))
hepta.add_participation(Heptathlon(p_ikauniece, Participant("Ikauniece", "Laura", 0, "LAT")))
hepta.add_participation(Heptathlon(p_schafer, Participant("Schäfer", "Carolin", 0, "GER")))
hepta.add_participation(Heptathlon(p_johnson_thompson, Participant("Johnson-Thompson", "Katarina", 0, "GBR")))
hepta.add_participation(Heptathlon(p_rodriguez, Participant("Rodríguez", "Yorgelis", 0, "CUB")))
hepta.add_participation(Heptathlon(p_farkas, Participant("Zsivoczky-Farkas", "Györgyi", 0, "HUN")))
hepta.add_participation(Heptathlon(p_oeser, Participant("Oeser", "Jennifer", 0, "HUN")))
hepta.add_participation(Heptathlon(p_vetter, Participant("Vetter", "Anouk", 0, "NED")))
hepta.add_participation(Heptathlon(p_nana_djimou, Participant("Nana Djimou", "Antoinnette", 0, "FRA")))
save.sauvegarder(hepta, hepta.nom)

print("Fichiers d'exemple générés !")