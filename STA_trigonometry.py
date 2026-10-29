import math

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Try Again")
            
def angle_from_sine():
    opposite = get_number("Enter the opposite side: ")
    hypotenuse = get_number("Enter the hypotenuse: ")

    angle = math.degrees(math.asin(opposite / hypotenuse))

    print("The angle is", angle)
    return angle

def angle_from_cosine():
    adjacent = get_number("Enter the adjacent side: ")
    hypotenuse = get_number("Enter the hypotenuse: ")

    angle = math.degrees(math.acos(adjacent / hypotenuse))

    print("The angle is", angle)
    return angle

def angle_from_tangent():
    opposite = get_number("Enter the opposite side: ")
    adjacent = get_number("Enter the adjacent side: ")

    angle = math.degrees(math.atan(opposite / adjacent))

    print("The angle is", angle)
    return angle

def opposite_from_sine():
    angle = get_number("Enter the angle: ")
    hypotenuse = get_number("Enter the hypotenuse: ")

    opposite = math.sin(math.radians(angle)) * hypotenuse

    print("The opposite side is", opposite)
    return opposite

def adjacent_from_cosine():
    angle = get_number("Enter the angle: ")
    hypotenuse = get_number("Enter the hypotenuse: ")

    adjacent = math.cos(math.radians(angle)) * hypotenuse

    print("The adjacent side is", adjacent)
    return adjacent

def opposite_from_tangent():
    angle = get_number("Enter the angle: ")
    adjacent = get_number("Enter the adjacent side: ")

    opposite = math.tan(math.radians(angle)) * adjacent

    print("The opposite side is", opposite)
    return opposite

def hypotenuse_from_sine():
    angle = get_number("Enter the angle: ")
    opposite = get_number("Enter the opposite side: ")

    hypotenuse = opposite / math.sin(math.radians(angle))

    print("The hypotenuse is", hypotenuse)
    return hypotenuse

def hypotenuse_from_cosine():
    angle = get_number("Enter the angle: ")
    adjacent = get_number("Enter the adjacent side: ")

    hypotenuse = adjacent / math.cos(math.radians(angle))

    print("The hypotenuse is", hypotenuse)
    return hypotenuse