y = [51, 6, 72, 83, 9, 36, 49]
max_1 = y[0]
for i in range(1, len(y)):
    if y[i] > max_1:
        max_1 = y[i]
print(max_1)
