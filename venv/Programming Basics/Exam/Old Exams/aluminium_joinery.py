number_of_joinery = int(input())
type_of_joinery = input()
type_of_delivery = input()
price = 0

if type_of_joinery.lower() == '90x130':
    price = 110
    if number_of_joinery in range(30, 61):
        price = price - price * 0.05
    elif number_of_joinery > 60:
        price = price - price * 0.08
elif type_of_joinery.lower() == '100x150':
    price = 140
    if number_of_joinery in range(40, 81):
        price = price - price * 0.06
    elif number_of_joinery > 80:
        price = price - price * 0.10
elif type_of_joinery.lower() == '130x180':
    price = 190
    if number_of_joinery in range(20, 51):
        price = price - price * 0.07
    elif number_of_joinery > 50:
        price = price - price * 0.12
elif type_of_joinery.lower() == '200x300':
    price = 250
    if number_of_joinery in range(25, 51):
        price = price - price * 0.09
    elif number_of_joinery > 50:
        price = price - price * 0.14

total_price = number_of_joinery * price

if type_of_delivery.capitalize() == 'With delivery':
    total_price = total_price + 60
elif type_of_delivery.capitalize() == 'Without delivery':
    total_price = total_price

if number_of_joinery > 99:
    total_price = total_price - (total_price * 0.04)
    print(f"{total_price:.2f} BGN")
elif number_of_joinery < 10:
    print("Invalid order")
else:
    print(f"{total_price:.2f} BGN")
