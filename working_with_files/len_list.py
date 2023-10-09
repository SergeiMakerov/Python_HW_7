from md_name import rnd_num
from md_name import rnd_name_in_file


def len_list(list1, list2):
    if len(list2) > len(list1):
        temp = len(list1)
    for i in range(len(list2)):
        if i > len(list1) - 1:
            list1.append(list1[i % temp])
        elif len(list2) < len(list1):
            temp = len(list2)
    for i in range(len(list1)):
        if i > len(list2) - 1:
            list2.append(list2[i % temp])
    return list1, list2
