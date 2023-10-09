from Fales.md_name import rnd_name
from random import randint


def create_files(extension, max_len_name=30, min_len_name=6, min_byte=256, max_byte=4096, qty_file=42):
    for _ in range(qty_file):
        with open(rnd_name() + extension, 'w') as f:
            f.write(str(bytes([randint(0, 255)
                    for _ in range(randint(min_byte, max_byte))])))


if __name__ == '__main__':
    create_files('file1.txt')
