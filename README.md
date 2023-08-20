# img2ascii
Membuat ASCII Art dari gambar.

# Usage

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
