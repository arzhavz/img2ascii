"""
ASCII Art Generator

Menghasilkan ASCII Art dari gambar dengan
kustomisasi ukuran dan karakter yang digunakan.

Author: Sandy Pratama
Date: 25 March 2023


Functions:
	- __init__(self, chars: List[str]) -> None:
		Konstruktor dari kelas ASCIIArtGenerator.
		
		Args:
			- chars (List[str]):
				Daftar karakter ASCII yang akan digunakan untuk membuat ASCII Art.
		
		Return:
			- None
		
	- generate_ascii_art(self, image_path: str, percentage: float = 100, new_width: int = None, new_height: int = None) -> str:
		Definisi untuk membuat ASCII Art dari input yang diberikan.
		
		Args:
			- image_path (str):
				Path atau lokasi gambar yang akan diubah menjadi ASCII Art.
			- percentage (float): 
				Persentase ukuran ASCII Art yang akan dihasilkan dari ukuran asli gambar. Akan diabaikan jika mengisi input new_height atau new_width.
			- new_height (int):
				Ukuran tinggi ASCII Art yang akan dibuat. Ukuran adalah jumlah karakter. Jika tidak terisi, akan menggunakan nilai dari percentage.
			- new_height (int):
				Ukuran lebar ASCII Art yang akan dibuat. Ukuran adalah jumlah karakter. Jika tidak terisi, akan menggunakan nilai dari percentage.
				
		Return:
			- str
				ASCII Art yang dihasilkan.
				
	- display(self, ascii_art: str, delay: float = 0.001) -> None:
		Menganimasikan ASCII Art ke konsol seperti ketikan.
		
		Args:
			- ascii_art (str):
				String ASCII Art yang ingin ditampilkan ke konsol.
			- delay (float):
				Selang waktu perkarakter yang ditampilkan ke konsol.
		
		Return:
			- None
			
	- save(self, id: int, ascii_art: str) -> None:
		Menyimpan atau menambahkan ASCII Art yang sudah dihasilkan kedalam file TXT dengan nama file ID.
		
		Args:
			- id (int):
				Id ASCII Art yang dihasilkan.
			- ascii_art (str):
				String yang ingin disimpan ke dalam file.
				
		Return:
			- None
"""


import time
import sys
import json
from typing import List
from io import BytesIO
from PIL import Image

from utils import RandID


class ASCIIArtGenerator:
    def __init__(self, chars: List[str]):
        self.chars = chars

    def generate_ascii_art(self, image_path: str, percentage: float = 100, new_width: int = None, new_height: int = None) -> str:
        try:
            with open(image_path, "rb") as f:
                img_data = f.read()

            img = Image.open(BytesIO(img_data))
            width, height = img.size

            if new_width is None and new_height is None:
                new_width = int(width * percentage / 100)
                new_height = int(height * percentage / 100)
            elif new_width is None:
                new_width = int(new_height * width / height)
            elif new_height is None:
                new_height = int(new_width * height / width)

            img = img.resize((new_width, new_height))
            img = img.convert("L")

            ascii_art = ""
            for y in range(new_height):
                for x in range(new_width):
                    pixel = img.getpixel((x, y))
                    char = self.chars[int(pixel / 25)]
                    ascii_art += char
                ascii_art += "\n"

            return ascii_art

        except Exception as e:
            raise e

    def display(self, ascii_art: str, delay: float = 0.001) -> None:
        for char in ascii_art:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)

    def save(self, ascii_art: str) -> None:
        try:
            with open(f"{RandID(20)}.txt", "w") as file:
            	file.write(ascii_art)
        except Exception as e:
        	raise e