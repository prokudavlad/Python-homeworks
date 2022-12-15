import math
print('Введіть коефіцієнт для рівняння')
print('ax^2 + bx + c = 0:')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
discriminator = b ** 2 - 4 * a * c
print('Дискримінант D = ', discriminator)
if discriminator > 0:
    x1 = (-b + math.sqrt(discriminator)) / (2 * a)
    x2 = (-b - math.sqrt(discriminator)) / (2 * a)
    print(f'x1 = {x1:.2f} ', 'x1 = ', x1)
    print(f'x2 = {x2:.2f}', 'x2 = ', x2)
elif discriminator == 0:
    x = -b / (2 * a)
    print('x = ', x)
else:
    print('Корні відсутні')