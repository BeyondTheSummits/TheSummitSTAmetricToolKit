import statistics

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Try Again")
            
def mean():
    numbers = []
    count = int(get_number("How many numbers? "))
    for _ in range(count):
        numbers.append(get_number("Enter a number: "))
    mean = sum(numbers) / len(numbers)
    print("The mean is", mean)
    return mean

def median():
    numbers = []
    count = int(get_number("How many numbers? "))
    for _ in range(count):
        numbers.append(get_number("Enter a number: "))
    median = statistics.median(numbers)
    print("The median is", median)
    return median

def mode():
    numbers = []
    count = int(get_number("How many numbers? "))
    for _ in range(count):
        numbers.append(get_number("Enter a number: "))
    mode = statistics.mode(numbers)
    print("The mode is", mode)
    return mode

def range_numbers():
    numbers = []
    count = int(get_number("How many numbers? "))
    for _ in range(count):
        numbers.append(get_number("Enter a number: "))
    range_value = max(numbers) - min(numbers)
    print("The range is", range_value)
    return range_value

def sum_numbers():
    numbers = []
    count = int(get_number("How many numbers? "))
    for _ in range(count):
        numbers.append(get_number("Enter a number: "))
    total = sum(numbers)
    print("The sum is", total)
    return total

def count_numbers():
    numbers = []
    count = int(get_number("How many numbers? "))
    for _ in range(count):
        numbers.append(get_number("Enter a number: "))
    total_count = len(numbers)
    print("The count is", total_count)
    return total_count

def minimum():
    numbers = []
    count = int(get_number("How many numbers? "))
    for _ in range(count):
        numbers.append(get_number("Enter a number: "))
    minimum = min(numbers)
    print("The minimum value is", minimum)
    return minimum

def maximum():
    numbers = []
    count = int(get_number("How many numbers? "))
    for _ in range(count):
        numbers.append(get_number("Enter a number: "))
    maximum = max(numbers)
    print("The maximum value is", maximum)
    return maximum

