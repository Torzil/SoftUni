beverage = input()
sugar_amount = input()
number_of_beverages = int(input())
beverage_price = 0

if beverage == "Espresso":
    if sugar_amount == "Without":
        beverage_price = 0.9
    elif sugar_amount == "Normal":
        beverage_price = 1
    elif sugar_amount == "Extra":
        beverage_price = 1.2
elif beverage == "Cappuccino":
    if sugar_amount == "Without":
        beverage_price = 1
    elif sugar_amount == "Normal":
        beverage_price = 1.2
    elif sugar_amount == "Extra":
        beverage_price = 1.6
elif beverage == "Tea":
    if sugar_amount == "Without":
        beverage_price = 0.5
    elif sugar_amount == "Normal":
        beverage_price = 0.6
    elif sugar_amount == "Extra":
        beverage_price = 0.7

total_price = number_of_beverages * beverage_price

if sugar_amount == "Without":
    total_price *= 0.65
if beverage == "Espresso" and number_of_beverages >= 5:
    total_price *= 0.75
if total_price > 15:
    total_price *= 0.8

print(f"You bought {number_of_beverages} cups of {beverage} for {total_price:.2f} lv.")
