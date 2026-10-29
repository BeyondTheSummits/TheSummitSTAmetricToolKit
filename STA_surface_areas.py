import math

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Try Again")
            
def surface_area_cube():
    side = get_number("Enter the side length: ")
    surface_area = 6 * side ** 2
    print("The surface area of the cube is", surface_area)
    return surface_area

def surface_area_cuboid():
    length = get_number("Enter the length: ")
    width = get_number("Enter the width: ")
    height = get_number("Enter the height: ")

    surface_area = 2 * (
        length * width +
        length * height +
        width * height
    )

    print("The surface area of the cuboid is", surface_area)
    return surface_area

def surface_area_sphere():
    radius = get_number("Enter the radius: ")

    surface_area = 4 * math.pi * radius ** 2

    print("The surface area of the sphere is", surface_area)
    return surface_area

def surface_area_cylinder():
    radius = get_number("Enter the radius: ")
    height = get_number("Enter the height: ")

    surface_area = (
        2 * math.pi * radius ** 2 +
        2 * math.pi * radius * height
    )

    print("The surface area of the cylinder is", surface_area)
    return surface_area

def surface_area_cone():
    radius = get_number("Enter the radius: ")
    slant_height = get_number("Enter the slant height: ")

    surface_area = (
        math.pi * radius ** 2 +
        math.pi * radius * slant_height
    )

    print("The surface area of the cone is", surface_area)
    return surface_area

def surface_area_hemisphere():
    radius = get_number("Enter the radius: ")

    surface_area = 3 * math.pi * radius ** 2

    print("The surface area of the hemisphere is", surface_area)
    return surface_area

def surface_area_pyramid():
    base_area = get_number("Enter the base area: ")
    perimeter = get_number("Enter the base perimeter: ")
    slant_height = get_number("Enter the slant height: ")

    surface_area = base_area + (0.5 * perimeter * slant_height)

    print("The surface area of the pyramid is", surface_area)
    return surface_area

def surface_area_prism():
    perimeter = get_number("Enter the cross-sectional perimeter: ")
    area = get_number("Enter the cross-sectional area: ")
    length = get_number("Enter the prism length: ")

    surface_area = (perimeter * length) + (2 * area)

    print("The surface area of the prism is", surface_area)
    return surface_area
