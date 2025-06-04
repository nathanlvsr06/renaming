#!/usr/bin/python3

import os
import shutil
from time import sleep

from rename_images import RenameImages
from prefix import Prefix

def main():

    prefix = None
    folder_path = None
    mode = None

    print("\n")
    print("======================== Renaming ========================")
    print("")

    while True:

        print("")
        print("0/ Copier les fichiers originaux ")
        print("1/ Configurer le préfixe")
        print("2/ Configurer le renommage")
        print("3/ Simuler")
        print("4/ Executer")
        print("5/ Quitter")

        try:
            choice = int(input())

            if choice == 0:
                print("")
                print("====== Copie des fichiers originaux ======")
                folder_path = copy(folder_path)
            elif choice == 1:
                print("")
                print("====== Configuration du préfixe =======")
                prefix = prefix_config()
            elif choice == 2:
                print("")
                print("====== Configuration du renommage =======")
                folder_path, mode = renaming_config(folder_path)
            elif choice == 3:
                if not prefix:
                    print("Vous devez configurer le préfixe avant cette étape !")
                elif not mode and folder_path:
                    print("Vous devez configurer le renommage avant cette étape !")
                else:
                    print("")
                    print("====== Simulation ======")
                    do_simulation(prefix, folder_path, mode)
            elif choice == 4:
                if not prefix:
                    print("Vous devez configurer le préfixe avant cette étape !")
                elif not mode and folder_path:
                    print("Vous devez configurer le renommage avant cette étape !")
                else:
                    ready = input("Êtes-vous prêt ? (y/N) ")
                    if ready.casefold() == 'y':
                        print("Renommage en cours...")
                        sleep(2)
                        RenameImages(prefix, folder_path, mode)
            elif choice == 5:
                return
            else:
                print("Choisisser une valeur entre 1 et 5")
        except ValueError:
            print("Saisie incorrecte")
        except KeyboardInterrupt:
            return

def prefix_config():
    satisfied = 'n'
    while satisfied == 'n':
        print("Etablissement du préfixe sous la forme: \n AAMMJJ EVENT_Name_Surname-number")
        surname = input("Votre prénom : ")
        name = input("Votre nom : ")
        number = input("Votre numéro : ")
        event = input("Abréviation de l'évènement : ")
        date = input("Date de l'évènement (AAMMJJ) : ")
        prefix = Prefix(surname, name, number, date, event)
        print(f"Voici le préfixe : {prefix}")
        satisfied = input("Êtes-vous satisfait ? (Y/n) ")
    return prefix

def renaming_config(path) -> None:
    if not path:
        path = input("Chemin du répertoire : ")
    if os.path.exists(path):
        if os.path.isdir(path):
            mode = choose_mode()
            return path, mode
        else:
            print(f"Erreur: le chemin {path} doit être un répertoire.")
            return renaming_config()
    else:
        print(f"Erreur: le chemin {path} n'est pas trouvé.")
        return renaming_config()

def do_simulation(prefix, folder_path, mode) -> bool:
    sleep(1)
    RenameImages(prefix, folder_path, mode, True)
    return
    
def choose_mode():
    mode = input("Comment voulez-vous renommer vos photos ? (date/name) ")
    if mode.casefold() != "date" and mode.casefold() != "name":
        print(f"Le mode {mode} n'est pas correct. Veuillez choisir entre date et name.")
        choose_mode()
    elif not mode:
            print("Vous devez selectionner un mode !")
            choose_mode()
    return mode

def copy(origin_path):
    if not origin_path:
        origin_path = input("Où se trouve vos fichiers ? (chemin vers le répertoire) ")

    copy_path = input("Vers quel dossier (existant ou inexistant) voulez-vous copier vos fichiers ? ")
    if os.path.exists(copy_path):
        copy_files(origin_path, copy_path)
    else:
        create_folder = input("Dossier inexistant, voulez vous créer ce dossier ? (Y/n) ")
        if create_folder.casefold() == 'n':
            copy()
        else:
            os.makedirs(copy_path)
            copy_files(origin_path, copy_path)
    return origin_path

def copy_files(source_dir: os.path, destination_dir: os.path) -> None:
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(destination_dir, filename)
        
        if os.path.isfile(source_path):  
            shutil.copy2(source_path, destination_path)


if __name__ == '__main__':
    main()