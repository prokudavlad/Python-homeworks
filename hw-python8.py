def quadrant(x, y):
    print("Введіть координати точки:")
    x = float(input("x = "))
    y = float(input("y = "))
    if (x > 0 and y > 0):
        print("Lines in First quadrant")
    elif (x < 0 and y > 0):
        print("Lines in Second quadrant")
    elif (x < 0 and y < 0):
       print("Lines in Third quadrant")
    elif (x > 0 and y < 0):
        print("Lines in Fourth quadrant")
    elif (x == 0 and y > 0):
        print("Lines at positive y axis")
    elif (x == 0 and y < 0):
        print("Lines at negative x axis")
    elif (y == 0 and x > 0):
        print("Lines at positive x axis")
x = 2
y = 3
quadrant(x, y)