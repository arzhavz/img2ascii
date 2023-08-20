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
