# img2ascii
Membuat ASCII Art dari gambar.

```python
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
```

# Usage as Class

```python
# Import kelas ASCIIArtGenerator
from generator import ASCIIArtGenerator

# Daftar seluruh karakter
chars = ["@", "#", "8", "&", "o", ":", "*", ".", " "]

# Buat objek generator dengan karakter tadi
Generator = ASCIIArtGenerator(chars)

# Path gambar kamu
image_path = "path/to/your/image.jpg"

# Menghasilkan ASCII art dari gambar tadi dengan tinggi 100 karakter dan lebar 200 karakter
ascii_art = Generator.generate_ascii_art(image_path, new_height=100, new_width=200)

# Menampilkan ASCII art di konsol dengan delay perkarakter 0.001 detik
Generator.display(ascii_art, delay=0.001)
```

# Usage as CLI

```sh
python sample.py --path path/to/your/image.jpg
```
