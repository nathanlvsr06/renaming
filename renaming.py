#!/usr/bin/python3

from rename_images import RenameImages
from prefix import Prefix
import os
from time import sleep

def main():

    prefix = None
    folder_path = None
    mode = None

    while True:

        print("")
        print("====== Renaming ======")
        print("")
        print("1/ Configurer le préfixe")
        print("2/ Configurer le renommage")
        print("3/ Simuler")
        print("4/ Executer")
        print("5/ Quitter")

        try:
            choice = int(input())


            if choice == 1:
                prefix = prefix_config()
            elif choice == 2:
                if not prefix:
                    print("Vous devez configurer le préfixe avant cette étape !")
                else:
                    folder_path, mode = renaming_config(prefix)
            elif choice == 3:
                if not prefix:
                    print("Vous devez configurer le préfixe avant cette étape !")
                elif not mode and folder_path:
                    print("Vous devez configurer le renommage avant cette étape !")
                else:
                    do_simulation(prefix, folder_path, mode)
            elif choice == 4:
                if not prefix:
                    print("Vous devez configurer le préfixe avant cette étape !")
                elif not mode and folder_path:
                    print("Vous devez configurer le renommage avant cette étape !")
                else:
                    ready = input("Êtes-vous prêt ? (y/N) ")
                    if ready.casefold() == 'y':
                        RenameImages(prefix, folder_path, mode)
            elif choice == 5:
                return
            else:
                print("Choisisser une valeur entre 1 et 5")
        except ValueError:
            print("Saisie incorrecte")

def prefix_config():
    satisfied = 'n'
    while satisfied == 'n':
        print("====== Configuration du préfixe =======")
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

def renaming_config(prefix) -> None:
    print("====== Configuration du renommage =======")
    path = input("Chemin du répertoire : ")
    if os.path.exists(path):
        if os.path.isdir(path):
            mode = choose_mode()
            return path, mode
        else:
            raise PathNotDirExcpetion(f"Erreur: le chemin {path} doit être un répertoire.")
    else:
        raise PathNotFoundException(f"Erreur: le chemin {path} n'est pas trouvé.")

def do_simulation(prefix, folder_path, mode) -> bool:
    print("====== Simulation ======")
    sleep(1)
    RenameImages(prefix, folder_path, mode, True)
    return
    
def choose_mode():
    mode = input("Comment voulez-vous renommer vos photos ? (date/name) ")
    if mode.casefold() != "date" and mode.casefold() != "name":
        raise ModeException(f"Le mode {mode} n'est pas correct.")
    elif not mode:
            raise ModeException("Vous devez selectionner un mode !")
    return mode
            

class PathNotFoundException(Exception):
    ''' Exception levée lorsqu'un chemin n'est pas trouvé. '''

class PathNotDirExcpetion(Exception):
    ''' Exception levée lorsqu'un chemin n'est pas un répertoire. '''

class ModeException(Exception):
    ''' Exception levée lorsque le mode n'est pas trouvée ou qu'il est faux. '''

if __name__ == '__main__':
    main()