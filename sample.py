from generator import ASCIIArtGenerator

# Daftar seluruh karakter ASCII
all_ascii_chars = ["@", "#", "8", "&", "o", ":", "*", ".", " "]
for i in range(32, 127):
    all_ascii_chars.append(chr(i))

# Buat objek generator dengan seluruh karakter ASCII
ascii_generator = ASCIIArtGenerator(all_ascii_chars)

# Path menuju gambar yang akan diubah menjadi seni ASCII
image_path = input(">> ")

# Generate seni ASCII dari gambar dengan lebar dan tinggi baru
ascii_art = ascii_generator.generate_ascii_art(image_path, new_height=100, new_width=200)

# Tampilkan seni ASCII dengan efek tulisan satu per satu
ascii_generator.display(ascii_art, delay=0.000001)

# Simpan seni ASCII ke dalam file teks
ascii_generator.save(ascii_art)
