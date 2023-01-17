lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(lst) // 2):
    lst[i], lst[-1 - i] = lst[-1 - i], lst[i]
print(lst)