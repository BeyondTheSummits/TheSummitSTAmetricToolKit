import math

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Try Again")
            
def perimeter_regular_polygon():
    sides = get_number("Enter the number of sides: ")
    side_length = get_number("Enter the side length: ")
    perimeter = sides * side_length
    print("The perimeter of the regular polygon is", perimeter)
    return perimeter

def perimeter_triangle():
    side1 = get_number("Enter side 1: ")
    side2 = get_number("Enter side 2: ")
    side3 = get_number("Enter side 3: ")
    perimeter = side1 + side2 + side3
    print("The perimeter of the triangle is", perimeter)
    return perimeter

def circumference_circle():
    radius = get_number("Enter the radius: ")
    circumference = 2 * math.pi * radius
    print("The circumference of the circle is", circumference)
    return circumference

def perimeter_square():
    side = get_number("Enter the side length: ")
    perimeter = 4 * side
    print("The perimeter of the square is", perimeter)
    return perimeter

def perimeter_parallelogram():
    base = get_number("Enter the base: ")
    side = get_number("Enter the side length: ")
    perimeter = 2 * (base + side)
    print("The perimeter of the parallelogram is", perimeter)
    return perimeter

def perimeter_trapezium():
    side1 = get_number("Enter side 1: ")
    side2 = get_number("Enter side 2: ")
    side3 = get_number("Enter side 3: ")
    side4 = get_number("Enter side 4: ")
    perimeter = side1 + side2 + side3 + side4
    print("The perimeter of the trapezium is", perimeter)
    return perimeter

def perimeter_rhombus():
    side = get_number("Enter the side length: ")
    perimeter = 4 * side
    print("The perimeter of the rhombus is", perimeter)
    return perimeter

def perimeter_kite():
    side1 = get_number("Enter the first side length: ")
    side2 = get_number("Enter the second side length: ")
    perimeter = (2 * side1) + (2 * side2)
    print("The perimeter of the kite is", perimeter)
    return perimeter