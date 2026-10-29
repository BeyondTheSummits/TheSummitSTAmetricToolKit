import math

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Try Again")
            
def probability():
    favourable = get_number("Enter favourable outcomes: ")
    total = get_number("Enter total outcomes: ")
    probability = favourable / total
    print("The probability is", probability)
    return probability

def probability_percentage():
    favourable = get_number("Enter favourable outcomes: ")
    total = get_number("Enter total outcomes: ")
    probability = (favourable / total) * 100
    print("The probability percentage is", probability)
    return probability

def dice_probability():
    favourable = get_number("Enter favourable outcomes: ")
    probability = favourable / 6
    print("The probability is", probability)
    return probability

def coin_probability():
    favourable = get_number("Enter favourable outcomes: ")
    probability = favourable / 2
    print("The probability is", probability)
    return probability

def permutations():
    n = int(get_number("Enter n: "))
    r = int(get_number("Enter r: "))
    permutations = math.factorial(n) / math.factorial(n - r)
    print("The permutations are", permutations)
    return permutations

def combinations():
    n = int(get_number("Enter n: "))
    r = int(get_number("Enter r: "))
    combinations = math.factorial(n) / (math.factorial(r) * math.factorial(n - r))
    print("The combinations are", combinations)
    return combinations