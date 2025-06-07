@echo off
echo Vérification de PyInstaller...

where pyinstaller >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo PyInstaller non trouvé. Installation en cours...
    pip install pyinstaller
) ELSE (
    echo PyInstaller est déjà installé.
)

echo.
echo Construction de l'exécutable...

REM Supprime les anciens fichiers si présents
rmdir /s /q build
rmdir /s /q dist
del renaming.spec 2>nul

pyinstaller --onefile renaming.py

echo.
echo Terminé ! Exécutable disponible dans le dossier dist\
pause
