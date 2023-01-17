from random import randint
arr = [randint(1, 100) for i in range(15)]
s, pr = 0, 1
for i in arr:
    s += i
    pr *= i
print(f'Список: {arr}\nПроизведение всех'
      f' элементов списка: {pr}\nСумма всех'
      f' элементов списка: {s}'
)