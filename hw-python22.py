def swappositions(lst, lst1, lst2):
    lst[lst1], lst[lst2] = lst[lst2], lst[lst1]
    return lst


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pos1, pos2 = 1, 10
print(swappositions(num, pos1 - 1, pos2 - 1))

