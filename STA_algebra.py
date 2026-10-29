import math

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Try Again")
            
def powers():
    number = get_number("Enter a number: ")
    power = get_number("Enter a power: ")
    answer = number ** power
    print("The answer is", answer)
    return answer

def square_root():
    number = get_number("Enter a number: ")
    answer = math.sqrt(number)
    print("The square root is", answer)
    return answer

def cube_root():
    number = get_number("Enter a number: ")
    answer = number ** (1/3)
    print("The cube root is", answer)
    return answer

def logarithm():
    number = get_number("Enter a number: ")
    answer = math.log10(number)
    print("The logarithm is", answer)
    return answer

def linear_equation():
    print("for ax + b = c")
    a = get_number("Enter a: ")
    b = get_number("Enter b: ")
    c = get_number("Enter c: ")
    x = (c - b) / a
    print("x =", x)
    return x

