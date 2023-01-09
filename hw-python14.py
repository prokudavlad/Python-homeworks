my_list = ['2', '8', '3', '4', '5', '1', '0', '7', '6', ]
x = str(input('Input x: '))
for i in my_list:
    if i == x:
        print('Ok!')
        break
    else:
        print('No!')