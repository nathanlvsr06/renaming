# Renaming – Utilitaire de renommage d’images

Ce projet Python permet de **renommer facilement des fichiers image** (ou tout autre fichier) dans un répertoire donné. Il est interactif, fonctionne dans le terminal, et guide l’utilisateur étape par étape.

> ✅ Compatible Windows, Linux, macOS  
> ✅ Utilisable en script Python ou sous forme d’exécutable

---

## 📦 Fonctionnalités

- Copie des fichiers originaux dans un dossier de travail
- Génération automatique de préfixes personnalisés (nom, prénom, date, événement, numéro)
- Deux modes de renommage :
  - Par date
  - Par nom de fichier original
- Simulation avant exécution
- Exécutable portable (via PyInstaller)

---

## 🛠️ Installation rapide

### 1. Cloner ce dépôt

Ouvre un terminal (ou Git Bash sur Windows) :

```bash
git clone https://github.com/nathanlvsr06/renaming.git
cd renaming
```

---

## 🧱 Création de l'exécutable

Deux scripts sont fournis pour simplifier la création de l’exécutable :

### 🪟 Windows

Lance ce fichier dans PowerShell ou le terminal Windows :

```bash
build.bat
```

Ce script :
- Installe PyInstaller si besoin
- Crée un exécutable unique dans le dossier `dist/`

Tu pourras ensuite lancer l’application avec :

```bash
dist\renaming.exe
```

---

### 🍎🐧 Linux / macOS

Dans ton terminal :

```bash
chmod +x build.sh
./build.sh
```

Ce script :
- Installe PyInstaller localement si besoin
- Crée un exécutable dans `dist/renaming`

Tu peux l’exécuter avec :

```bash
./dist/renaming
```

> 💡 Si une erreur de permission survient, exécute `chmod +x dist/renaming`.

---

## 🐍 Utilisation directe du script (développeurs)

Tu peux également lancer le script en mode Python :

```bash
python renaming.py
```

---

## 🎮 Mode d’emploi interactif

Une fois lancé, le programme affiche un menu :

```
======================== Renaming ========================

0/ Copier les fichiers originaux
1/ Configurer le préfixe
2/ Configurer le renommage
3/ Simuler
4/ Executer
5/ Quitter
```

Chaque étape est expliquée dans le terminal.

### Exemple de préfixe généré

```
240604 EVENT_Jean_Dupont-07
```

> Format : `AAMMJJ EVENT_Prenom_Nom-numero`

### Modes de renommage disponibles

- `name` : conserve le nom original du fichier
- `date` : renomme selon la date de création/modification

---

## 📁 Structure du projet

```
image-renamer/
├── renaming.py           # Script principal (menu interactif)
├── rename_images.py      # Logique de renommage
├── prefix.py             # Génération de préfixes
├── build.bat             # Script de build Windows
├── build.sh              # Script de build Linux/macOS
├── README.md             # Documentation
└── (dist/, build/, .spec) → générés automatiquement
```

---

## 🧼 Nettoyage des fichiers générés

Si tu veux supprimer les fichiers produits lors de la compilation :

### Linux/macOS

```bash
rm -rf build dist __pycache__ renaming.spec
```

### Windows

```bat
rmdir /s /q build dist __pycache__
del renaming.spec
```

---

## ❓ Besoin d’aide

Si tu rencontres un bug ou as une question, ouvre une *issue* dans le dépôt GitHub.

---

## 📜 Licence

Ce projet est open-source, publié sous licence MIT.
