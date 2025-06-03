#!/usr/bin/python3
''' Module proposant la classe RenameImages '''

import os
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
from prefix import Prefix

class RenameImages():
    ''' Classe RenameImages permettant de renommer toutes les images d'un répertoire selon un préfixe prédéfini '''
    def __init__(self, prefix: Prefix, folder_path: str, mode: str = 'date', simulation: bool = False) -> None:
        self._prefix = prefix
        self._folder_path = folder_path
        self._simulation = simulation
        self._mode = mode
        if self._mode == 'date':
            self.rename_images_by_date()
        elif self._mode == 'name':
            self.rename_images_by_name()

    @staticmethod
    def get_exif_datetime(image_path: str) -> datetime:
        ''' Retourne la date Exif d'une image '''
        try:
            image = Image.open(image_path)
            exif_data = image._getexif()
            if exif_data:
                for tag_id, value in exif_data.items():
                    tag = TAGS.get(tag_id)
                    if tag == 'DateTimeOriginal':
                        return datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
        except Exception as e:
            print(f"Erreur avec {image_path}: {e}")
        return None
    
    @staticmethod
    def extract_old_index(image_name: str) -> str:
        ''' Extrait les 4 derniers chiffres du nom du fichier '''
        try:
            name_part = os.path.splitext(image_name)[0]
            digits = ''.join(filter(str.isdigit, name_part))
            return digits[-4:] if len(digits) >= 4 else digits.zfill(4)
        except Exception as e:
            print(f"Erreur avec {image_name}: {e}")

    def is_simulation(self) -> bool:
        return self._simulation

    def rename_images_by_date(self):
        images = [f for f in os.listdir(self._folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        image_dates = []

        for img in images:
            path = os.path.join(self._folder_path, img)
            date = self.get_exif_datetime(path)
            if date:
                image_dates.append((img, date))
            else:
                print(f"Aucune date EXIF pour {img}, ignorée.")

        sorted_images = sorted(image_dates, key=lambda x: x[1])

        for i, (original_name, _) in enumerate(sorted_images, start=1):
            extension = os.path.splitext(original_name)[1].lower()
            old_index = self.extract_old_index(original_name)
            new_name = f"{self._prefix}{i:04d}-({old_index}){extension}"

            old_path = os.path.join(self._folder_path, original_name)
            new_path = os.path.join(self._folder_path, new_name)

            if self.is_simulation():
                print(f"[SIMULATION] {original_name} -> {new_name}")
            else:
                os.rename(old_path, new_path)
                print(f"Renommé : {original_name} -> {new_name}")

    def rename_images_by_name(self):
        images = [f for f in os.listdir(self._folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        sorted_images = sorted(images)

        for i, original_name in enumerate(sorted_images, start=1):
            extension = os.path.splitext(original_name)[1].lower()
            old_index = self.extract_old_index(original_name)
            new_name = f"{self._prefix}{i:04d}-({old_index}){extension}"

            old_path = os.path.join(self._folder_path, original_name)
            new_path = os.path.join(self._folder_path, new_name)

            if self.is_simulation():
                print(f"[SIMULATION] {original_name} -> {new_name}")
            else:
                os.rename(old_path, new_path)
                print(f"Renommé : {original_name} -> {new_name}")


        
    
if __name__ == '__main__':
    pass