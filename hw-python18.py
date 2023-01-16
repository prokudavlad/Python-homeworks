lst = [77, 3, 8, 96, 41]
lst_sum = 0
lst_mul = 1
for i in lst:
    lst_sum += i
    lst_mul *= i
print("Source List", *lst)
print("Sum of list elements =", lst_sum)
print("Product of list elements =", lst_mul)