#!/bin/bash

echo "Vérification de la présence de PyInstaller..."

# Vérifie si pyinstaller est accessible
if ! command -v pyinstaller &> /dev/null; then
    echo "PyInstaller non trouvé, installation en cours..."
    pip install --user pyinstaller
else
    echo "PyInstaller déjà installé."
fi

echo "Construction de l'exécutable..."

# Supprimer les anciennes builds s’il y en a
rm -rf build dist renaming.spec

# Construire l'exécutable
pyinstaller --onefile renaming.py

echo ""
echo "Terminé ! Exécutable disponible dans le dossier ./dist/"
