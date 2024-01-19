age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

total_toys = 0
total_birthday_money = 0
current_birthday_money = 0
saved_money = 0

for number in range(1, age + 1):
    if number % 2 == 0:
        current_birthday_money += 10
        total_birthday_money += current_birthday_money - 1
    else:
        total_toys += 1

saved_money += total_birthday_money + total_toys * toy_price
difference = abs(saved_money - washing_machine_price)

if saved_money >= washing_machine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
