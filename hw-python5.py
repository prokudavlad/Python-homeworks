import math
x = int(input())
if x > 0:
    y = 2 * x - 10
elif x < 0:
    y = int(2 * math.fabs(x) - 1)
else:
    y = 0
print('y')