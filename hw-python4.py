def isInside(circle_x, circle_y, radius, x, y):
    if ((x - circle_x) * (x - circle_x) +
            (y - circle_y) * (y - circle_y) <= radius * radius):
        return True
    else:
        return False


x = 1
y = 1
circle_x = 0
circle_y = 1
radius = 2

if (isInside(circle_x, circle_y, radius, x, y)):
    print("Inside")
else:
    print("Outside")