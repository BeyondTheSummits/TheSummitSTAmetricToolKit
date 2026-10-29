import math

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Try Again")
            
def volume_cube():
    side = get_number("Enter the side length: ")
    volume = side ** 3
    print("The volume of the cube is", volume)
    return volume

def volume_cuboid():
    length = get_number("Enter the length: ")
    width = get_number("Enter the width: ")
    height = get_number("Enter the height: ")
    volume = length * width * height
    print("The volume of the cuboid is", volume)
    return volume

def volume_sphere():
    radius = get_number("Enter the radius: ")
    volume = (4 / 3) * math.pi * radius ** 3
    print("The volume of the sphere is", volume)
    return volume

def volume_cylinder():
    radius = get_number("Enter the radius: ")
    height = get_number("Enter the height: ")
    volume = math.pi * radius ** 2 * height
    print("The volume of the cylinder is", volume)
    return volume

def volume_cone():
    radius = get_number("Enter the radius: ")
    height = get_number("Enter the height: ")
    volume = (1 / 3) * math.pi * radius ** 2 * height
    print("The volume of the cone is", volume)
    return volume

def volume_hemisphere():
    radius = get_number("Enter the radius: ")
    volume = (2 / 3) * math.pi * radius ** 3
    print("The volume of the hemisphere is", volume)
    return volume

def volume_pyramid():
    base_area = get_number("Enter the base area: ")
    height = get_number("Enter the height: ")
    volume = (1 / 3) * base_area * height
    print("The volume of the pyramid is", volume)
    return volume

def volume_prism():
    cross_section_area = get_number("Enter the cross-sectional area: ")
    length = get_number("Enter the length: ")
    volume = cross_section_area * length
    print("The volume of the prism is", volume)
    return volume