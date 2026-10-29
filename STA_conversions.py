def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Try Again")

def mm_to_cm():
    mm = get_number("Enter millimetres: ")
    cm = mm / 10
    print("The value in centimetres is", cm)
    return cm

def cm_to_mm():
    cm = get_number("Enter centimetres: ")
    mm = cm * 10
    print("The value in millimetres is", mm)
    return mm

def cm_to_m():
    cm = get_number("Enter centimetres: ")
    metres = cm / 100
    print("The value in metres is", metres)
    return metres

def m_to_cm():
    metres = get_number("Enter metres: ")
    cm = metres * 100
    print("The value in centimetres is", cm)
    return cm

def m_to_km():
    metres = get_number("Enter metres: ")
    km = metres / 1000
    print("The value in kilometres is", km)
    return km

def km_to_m():
    km = get_number("Enter kilometres: ")
    metres = km * 1000
    print("The value in metres is", metres)
    return metres

def mg_to_g():
    mg = get_number("Enter milligrams: ")
    g = mg / 1000
    print("The value in grams is", g)
    return g

def g_to_mg():
    g = get_number("Enter grams: ")
    mg = g * 1000
    print("The value in milligrams is", mg)
    return mg

def g_to_kg():
    g = get_number("Enter grams: ")
    kg = g / 1000
    print("The value in kilograms is", kg)
    return kg

def kg_to_g():
    kg = get_number("Enter kilograms: ")
    g = kg * 1000
    print("The value in grams is", g)
    return g

def kg_to_tonnes():
    kg = get_number("Enter kilograms: ")
    tonnes = kg / 1000
    print("The value in tonnes is", tonnes)
    return tonnes

def tonnes_to_kg():
    tonnes = get_number("Enter tonnes: ")
    kg = tonnes * 1000
    print("The value in kilograms is", kg)
    return kg

def kg_to_lb():
    kg = get_number("Enter kilograms: ")
    lb = kg * 2.20462
    print("The value in pounds is", lb)
    return lb

def lb_to_kg():
    lb = get_number("Enter pounds: ")
    kg = lb / 2.20462
    print("The value in kilograms is", kg)
    return kg

def celsius_to_fahrenheit():
    celsius = get_number("Enter Celsius: ")
    fahrenheit = (celsius * 9 / 5) + 32
    print("The value in Fahrenheit is", fahrenheit)
    return fahrenheit

def fahrenheit_to_celsius():
    fahrenheit = get_number("Enter Fahrenheit: ")
    celsius = (fahrenheit - 32) * 5 / 9
    print("The value in Celsius is", celsius)
    return celsius

def celsius_to_kelvin():
    celsius = get_number("Enter Celsius: ")
    kelvin = celsius + 273.15
    print("The value in Kelvin is", kelvin)
    return kelvin

def kelvin_to_celsius():
    kelvin = get_number("Enter Kelvin: ")
    celsius = kelvin - 273.15
    print("The value in Celsius is", celsius)
    return celsius

def fahrenheit_to_kelvin():
    fahrenheit = get_number("Enter Fahrenheit: ")
    kelvin = (fahrenheit - 32) * 5 / 9 + 273.15
    print("The value in Kelvin is", kelvin)
    return kelvin

def kelvin_to_fahrenheit():
    kelvin = get_number("Enter Kelvin: ")
    fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
    print("The value in Fahrenheit is", fahrenheit)
    return fahrenheit

def seconds_to_minutes():
    seconds = get_number("Enter seconds: ")
    minutes = seconds / 60
    print("The value in minutes is", minutes)
    return minutes

def minutes_to_seconds():
    minutes = get_number("Enter minutes: ")
    seconds = minutes * 60
    print("The value in seconds is", seconds)
    return seconds

def minutes_to_hours():
    minutes = get_number("Enter minutes: ")
    hours = minutes / 60
    print("The value in hours is", hours)
    return hours

def hours_to_minutes():
    hours = get_number("Enter hours: ")
    minutes = hours * 60
    print("The value in minutes is", minutes)
    return minutes

def hours_to_days():
    hours = get_number("Enter hours: ")
    days = hours / 24
    print("The value in days is", days)
    return days

def days_to_hours():
    days = get_number("Enter days: ")
    hours = days * 24
    print("The value in hours is", hours)
    return hours
