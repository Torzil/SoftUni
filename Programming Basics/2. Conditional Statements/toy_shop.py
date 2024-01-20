vacation_price = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

puzzle_price = 2.60
doll_price = 3.00
bear_price = 4.10
minion_price = 8.20
truck_price = 2.00

gross_profit = number_of_puzzles * puzzle_price \
    + number_of_dolls * doll_price \
    + number_of_bears * bear_price \
    + number_of_minions * minion_price \
    + number_of_trucks * truck_price

number_of_toys = number_of_puzzles + number_of_dolls \
    + number_of_bears + number_of_minions + number_of_trucks

if number_of_toys >= 50:
    gross_profit -= gross_profit * 0.25

rent_price = gross_profit * 0.1

net_profit = gross_profit - rent_price

difference = abs(net_profit - vacation_price)

if net_profit >= vacation_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
