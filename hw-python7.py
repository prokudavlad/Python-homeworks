x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
print("Input lengths of the triangle sides: ")

if x == y == z:
    print("Equilateral triangle")
elif x == y or z == y or x == z:
    print("isosceles triangle")
else:
    print("Scalene triangle")