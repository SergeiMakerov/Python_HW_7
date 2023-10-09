from md_name import rnd_num
from md_name import rnd_name_in_file
import len_list


def open_file(file_names, file_num, output):
    with (
            open(file_names, 'r') as a,
            open(file_num, 'r') as b,
            open(output, 'w') as c):
        names = a.read().split('\n')
    num = b.read().split('\n')
    for i, j in zip(*len_list(names, num)):
        if j == '':
            continue
    first, second = map(float, j.split('|'))
    mult = first * second
    if mult < 0:
        c.write(f'{i.lower()} {abs(mult)}\n')
    elif mult > 0:
        c.write(f'{i.upper()} {int(mult)}\n')

    if __name__ == '__main__':
        rnd_num(10, 'num1.txt')
        rnd_name_in_file(5, 'names1.txt')
        open_file('names1.txt', 'num1.txt', 'output.txt')
