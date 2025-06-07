@echo off
rmdir /s /q build
rmdir /s /q dist
del renaming.spec
pyinstaller --onefile renaming.py
