import math

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Try Again")
            
def hypotenuse():
    side1 = get_number("Enter side 1: ")
    side2 = get_number("Enter side 2: ")

    hypotenuse = math.sqrt(side1 ** 2 + side2 ** 2)

    print("The hypotenuse is", hypotenuse)
    return hypotenuse

def missing_side():
    hypotenuse = get_number("Enter the hypotenuse: ")
    known_side = get_number("Enter the known side: ")

    side = math.sqrt(hypotenuse ** 2 - known_side ** 2)

    print("The missing side is", side)
    return side