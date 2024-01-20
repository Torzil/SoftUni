fuel_type = input()
fuel_quantity = float(input())
discount_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93
total_price = 0

if fuel_type.capitalize() == "Gasoline":
    total_price = fuel_quantity * gasoline_price
    if discount_card.capitalize() == "Yes":
        total_price = total_price - fuel_quantity * 0.18
elif fuel_type.capitalize() == "Diesel":
    total_price = fuel_quantity * diesel_price
    if discount_card.capitalize() == "Yes":
        total_price = total_price - fuel_quantity * 0.12
elif fuel_type.capitalize() == "Gas":
    total_price = fuel_quantity * gas_price
    if discount_card.capitalize() == "Yes":
        total_price = total_price - fuel_quantity * 0.08

if 20 < fuel_quantity <= 25:
    total_price -= total_price * 0.08
elif fuel_quantity > 25:
    total_price -= total_price * 0.1

print(f"{total_price:.2f} lv.")
