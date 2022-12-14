num = int(input('How many numbers: '))
total_sum = 0
for n in range(num):
    numbers = float(input('Enter number : '))
    total_sum += numbers
avg = total_sum/num
print('Average of ', num, ' numbers is :', avg)

number = int(input("Enter number: "))
if number < 3.5:
    print("Your number is smaller than 3.5")
else:
    print("Your number is greater than 3.5")