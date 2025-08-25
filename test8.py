def read_point():
    print("For point (x,y):")
    x = float(input("Input x? "))
    y = float(input("Input y? "))
    return x, y

def localize(x, y):
    if x > 0 and y > 0:
        return 'in quadrant 1'
    elif x < 0 and y > 0:
        return 'in quadrant 2'
    elif x < 0 and y < 0:
        return 'in quadrant 3'
    elif x > 0 and y < 0:
        return 'in quadrant 4'
    elif x == 0 and (y > 0 or y < 0):
        return 'on the y-axis'
    elif (x > 0 or x < 0) and y == 0:
        return 'on the x-axis'
    elif x == 0 and y == 0:
        return 'at the origin'

x, y = read_point()
location = localize(x, y)
print(f"The location of ({x:.2f}, {y:.2f}) is {location}.")