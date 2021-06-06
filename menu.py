from Objects.Fichier import Fichier
from os import system
import os

from prettytable import PrettyTable
from simple_term_menu import TerminalMenu

from Objects.Competition import Competition
from Objects.Decathlon import Decathlon
from Objects.Participant import Participant

def ajouter_perfomances(compet_chargee):
    nom_athlete = input("Nom de l'athlète : ")
    prenom_athlete = input("Prénom de l'athlète : ")
    sexe_athlete_menu = TerminalMenu([
        "Femme 🚺",
        "Homme 🚹"
    ])
    sexe_athle = sexe_athlete_menu.show()
    nation_athle = input("Nation de " +nom_athlete+ " : ")
    if sexe_athle==1: # Homme
        nom_epreuves = [
            "1OOm (s)",
            "Longueur (m)",
            "Poids (m)"
            "Hauteur (m)",
            "400m (s)",
            "11O H (s)",
            "Disque (m)",
            "Perche (m)",
            "Javelot (m)",
            "1500m (s)"
            
        ]
    else:   # Femme
        nom_epreuves = [
            "1OOm H(s)",
            "Hauteur (m)",
            "Poids (m)"
            "200m (s)",
            "Longueur (m)",
            "Javelot (m)",
            "800m (s)"
        ]
    
    performances = []
    for epreuve in range(len(nom_epreuves)):
        performances.append(float(input("Perfomance -> "+nom_epreuves[epreuve]+" : ")))
    system('clear')

    print(" --- CONFIRMATION ---")
    print("ATHLETE : " +prenom_athlete+" "+nom_athlete+ " - " +nation_athle)
    confirm = PrettyTable()
    confirm.field_names = nom_epreuves
    confirm.add_row(performances)
    print(confirm)

    print("Confirmer l'ajout ?")
    add_confirmation = TerminalMenu([
        "OUI",
        "NON"
    ])
    confirm_choix = add_confirmation.show()

    if (confirm_choix == 0):
        compet_chargee.add_participation(Decathlon(performances, Participant(nom_athlete, prenom_athlete, int(sexe_athle), nation_athle)))
        print("Athlète ajouté(e) avec succès")
        
    else:
        print("Ajout annulé")
        pass

def load_competition():
    fichiers = Fichier(os.path.join(os.getcwd(), "storage"))
    compet = fichiers.explorer()
    print("Quelle compétition voulez-vous charger ?")
    load_menu = TerminalMenu(compet)
    compet_a_charger = load_menu.show()
    return fichiers.charger(compet[compet_a_charger])

def new_competition():
    nom_competition = input("Nom de la compétition : ")
    lieu_competition = input("Lieu de la compétition : ")
    print("Type d'épreuve ?")
    liste_type_competition = [
        "Décathlon",
        "Heptathlon"
    ]
    type_competition_menu = TerminalMenu(liste_type_competition)
    choix_type_competition = type_competition_menu.show()
    nouvelle_competition = Competition((nom_competition+"-"+liste_type_competition[choix_type_competition]), lieu_competition)
    save_competition(nouvelle_competition)
    print("Compétition ajoutée avec succée : pensez à la charger")
    
def save_competition(competition_a_sauvegarder):
    print("Voulez-vous sauvegarder la compétition ?")
    confirmation_save = TerminalMenu([
        "OUI",
        "NON"
    ])
    choix_confirmation = confirmation_save.show()
    
    if choix_confirmation==0:
        path = os.path.join(os.getcwd())
        fichier = Fichier(path)
        fichier.sauvegarder(competition_a_sauvegarder, competition_a_sauvegarder.nom)
    elif choix_confirmation==1:
        print("Sauvegarde annulée")

def details(compet_chargee):
    print("Rechercher par :")
    select_field = TerminalMenu([
        "Epreuves",
        "Athlete"
    ])
    field = select_field.show()

    # Par epreuve
    if (field == 0):
        list_ep_menu = []
        if len(compet_chargee.combined_event) > 0:
            for epreuve in range(len(compet_chargee.combined_event[0].perfs)):
                list_ep_menu.append(compet_chargee.combined_event[0].perfs[epreuve].nom)
            
            ep_menu = TerminalMenu(list_ep_menu)

            ep_index = ep_menu.show()

            system('clear')

            perfs = {}

            for ce in range(len(compet_chargee.combined_event)):
                perfs[compet_chargee.combined_event[ce].athlete.nom] = compet_chargee.combined_event[ce].perfs[ep_index].perf

            print("Récapitulatif pour " +list_ep_menu[ep_index])
            ep_details = PrettyTable()
            ep_details.field_names = ["Athlete", "Performance"]
            for athlete, performance in perfs.items():
                ep_details.add_row([athlete, performance])
            print(ep_details)
        
    # Par athlète
    elif (field == 1):
        liste_nom_athlete = []
        for ce in range(len(compet_chargee.combined_event)):
            liste_nom_athlete.append(compet_chargee.combined_event[ce].athlete.prenom+ " "+compet_chargee.combined_event[ce].athlete.nom)
        nom_athlete_menu = TerminalMenu(liste_nom_athlete)
        athlete = nom_athlete_menu.show()
        system("clear")
        print("Athlete : " +compet_chargee.combined_event[athlete].athlete.prenom+ " "+compet_chargee.combined_event[athlete].athlete.nom)
        resultats_athlete = PrettyTable()
        resultats_athlete.field_names = ["Epreuve", "Performance", "Score"]
        for epreuve in range(len(compet_chargee.combined_event[athlete].perfs)):
            resultats_athlete.add_row([
                compet_chargee.combined_event[athlete].perfs[epreuve].nom,
                compet_chargee.combined_event[athlete].perfs[epreuve].perf+" "+compet_chargee.combined_event[athlete].perfs[epreuve].unite,
                compet_chargee.combined_event[athlete].perfs[epreuve].score
            ])
        print(resultats_athlete)

def main():
    main_choix = None
    compet_chargee = load_competition()
    system("clear")
    while (main_choix!=6):
        print("--- ~ A FOND LA FORME ~ ---")
        print("Compétition chargée : " +compet_chargee.nom+ " (à " +compet_chargee.lieu+ ")")
        print("Que voulez-vous faire ?")

        main_menu = TerminalMenu([
            "Voir les résultats",
            "Ajouter des performances à une compétition existante",
            "Charger une compétition",
            "Créer une compétition",
            "Sauvegarder la compétition",
            "Voir des détails",
            "Quitter"
        ])
        main_choix = main_menu.show()

        system('clear')

        if (main_choix==0): # Voir les résultats
            compet_chargee.recap()
        elif (main_choix==1): # Ajouter performance
            ajouter_perfomances(compet_chargee)
        elif (main_choix==2): # Charger 
            compet_chargee = load_competition()
            print("La compétition " +compet_chargee.nom+ " (à " +compet_chargee.lieu+ ") a bien été chargée")
        elif (main_choix==3): # Créer compétition
            new_competition()
        elif (main_choix==4): # Sauvegarder
            save_competition(compet_chargee)
        elif (main_choix==5): # Voir détails
            details(compet_chargee)
        elif (main_choix==6): # Quitter
            pass

if __name__ == "__main__":
    main()
