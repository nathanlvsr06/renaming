#!/bin/bash

set -e

echo "Vérification ou création d'un environnement virtuel..."

# Créer le dossier s'il n'existe pas
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Environnement virtuel créé dans ./venv"
fi

# Activer l'environnement virtuel
source venv/bin/activate

# Vérifier pyinstaller dans l'env virtuel
if ! pip show pyinstaller &> /dev/null; then
    echo "Installation de PyInstaller dans l'environnement virtuel..."
    pip install --upgrade pip
    pip install pyinstaller
else
    echo "PyInstaller déjà installé dans l'environnement virtuel."
fi

echo "Nettoyage d'anciennes builds..."
rm -rf build dist renaming.spec

echo "Construction de l'exécutable..."
pyinstaller --onefile renaming.py

echo ""
echo "Terminé. Exécutable disponible dans le dossier ./dist/"
echo "Pour relancer manuellement :"
echo "source venv/bin/activate && pyinstaller --onefile renaming.py"
