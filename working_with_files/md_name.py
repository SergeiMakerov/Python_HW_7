from random import randint
VOWELS = "AEYUIOaeuioy"


def rnd_name():
    name_len = randint(4, 7)
    while True:
        name = ""
    for i in range(name_len):
        name += chr(randint(65, 90))
    for i in name:
        if i in VOWELS:
            return name.capitalize()


def rnd_name_in_file(count, file_name):
    with open(file_name, "a") as f:
        for i in range(count):
            f.write(rnd_name()+"\n")


rnd_name_in_file(5, 'md_name.py\names.txt')
