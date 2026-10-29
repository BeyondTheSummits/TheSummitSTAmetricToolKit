def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Try Again")
            
def percentage():
    value = get_number("Enter the value: ")
    total = get_number("Enter the total: ")
    percentage = (value / total) * 100
    print("The percentage is", percentage)
    return percentage

def percentage_increase():
    original = get_number("Enter the original value: ")
    new = get_number("Enter the new value: ")
    increase = ((new - original) / original) * 100
    print("The percentage increase is", increase)
    return increase

def percentage_decrease():
    original = get_number("Enter the original value: ")
    new = get_number("Enter the new value: ")
    decrease = ((original - new) / original) * 100
    print("The percentage decrease is", decrease)
    return decrease

def profit():
    cost_price = get_number("Enter the cost price: ")
    selling_price = get_number("Enter the selling price: ")
    profit = selling_price - cost_price
    print("The profit is", profit)
    return profit

def loss():
    cost_price = get_number("Enter the cost price: ")
    selling_price = get_number("Enter the selling price: ")
    loss = cost_price - selling_price
    print("The loss is", loss)
    return loss

def vat():
    price = get_number("Enter the original price: ")
    vat_rate = get_number("Enter the VAT percentage: ")
    total_price = price + (price * vat_rate / 100)
    print("The price including VAT is", total_price)
    return total_price

def discount():
    price = get_number("Enter the original price: ")
    discount_rate = get_number("Enter the discount percentage: ")
    discounted_price = price - (price * discount_rate / 100)
    print("The discounted price is", discounted_price)
    return discounted_price

def markup():
    cost_price = get_number("Enter the cost price: ")
    markup_percentage = get_number("Enter the markup percentage: ")
    selling_price = cost_price + (cost_price * markup_percentage / 100)
    print("The selling price is", selling_price)
    return selling_price

def markdown():
    price = get_number("Enter the original price: ")
    markdown_percentage = get_number("Enter the markdown percentage: ")
    new_price = price - (price * markdown_percentage / 100)
    print("The markdown price is", new_price)
    return new_price

def break_even():
    fixed_costs = get_number("Enter the fixed costs: ")
    selling_price = get_number("Enter the selling price per unit: ")
    variable_cost = get_number("Enter the variable cost per unit: ")

    units = fixed_costs / (selling_price - variable_cost)

    print("The break-even point is", units, "units")
    return units