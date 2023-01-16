lst = []
for i in range(100):
    lst.append('0')
lst[0] = '1'
lst[-1] = '1'
print(lst)