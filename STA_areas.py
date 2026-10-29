import math

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Try Again")

def area_regular_polygon():
    sides = get_number("Enter the number of sides: ")
    side_length = get_number("Enter the side length: ")
    apothem = side_length / (2 * math.tan(math.pi / sides))
    perimeter = sides * side_length
    area = (perimeter * apothem) / 2
    print("The area of the regular polygon is", area)
    return area

def area_rectangle():
    length = get_number("Enter the length: ")
    width = get_number("Enter the width: ")
    area = length * width
    print("The area of the rectangle is", area)
    return area

def area_triangle():
    height = get_number("Enter the height: ")
    base = get_number("Enter the base: ")
    area = 1/2 * height * base
    print("The area of the triangle is: ", area)
    return area

def area_circle():
    radius = get_number("Enter the radius: ")
    area = math.pi * radius ** 2
    print("The area of the circle is: ", area)
    return area

def area_square():
    side = get_number("Enter the side length: ")
    area = side ** 2
    print("The area of the square is", area)
    return area

def area_parallelogram():
    base = get_number("Enter the base: ")
    height = get_number("Enter the height: ")
    area = base * height
    print("The area of the parallelogram is", area)
    return area

def area_trapezium():
    side1 = get_number("Enter the first parallel side: ")
    side2 = get_number("Enter the second parallel side: ")
    height = get_number("Enter the height: ")
    area = ((side1 + side2) / 2) * height
    print("The area of the trapezium is", area)
    return area

def area_rhombus():
    diagonal1 = get_number("Enter diagonal 1: ")
    diagonal2 = get_number("Enter diagonal 2: ")
    area = (diagonal1 * diagonal2) / 2
    print("The area of the rhombus is", area)
    return area

def area_kite():
    diagonal1 = get_number("Enter diagonal 1: ")
    diagonal2 = get_number("Enter diagonal 2: ")
    area = (diagonal1 * diagonal2) / 2
    print("The area of the kite is", area)
    return area