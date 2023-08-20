import argparse
from generator import ASCIIArtGenerator

def main():
    all_ascii_chars = ["@", "#", "8", "&", "o", ":", "*", ".", " "]
    for i in range(32, 127):
        all_ascii_chars.append(chr(i))
    ascii_generator = ASCIIArtGenerator(all_ascii_chars)

    parser = argparse.ArgumentParser(description='Convert an image to ASCII art and display it with character delay.')

    parser.add_argument('--path', required=True, help='Path to the input image')
    parser.add_argument('--display', type=float, default=0.001, help='Character display delay in seconds')
    parser.add_argument('--save', action='store_true', help='Save the ASCII art to a text file')
    parser.add_argument('--width', type=int, help='Width of ASCII art (chars)', default=200)
    parser.add_argument('--height', type=int, help='Height of ASCII art (chars)', default=100)

    args = parser.parse_args()
    ascii_art = ascii_generator.generate_ascii_art(args.path, new_height=args.height, new_width=args.width)
    ascii_generator.display(ascii_art, delay=args.display)

    if args.save:
        ascii_generator.save(ascii_art)

if __name__ == '__main__':
    main()
