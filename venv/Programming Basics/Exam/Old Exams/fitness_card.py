available_money = float(input())
gender = input()
age = int(input())
sport = input()
price = 0

if gender.lower() == "m":
    if sport.lower() == "gym":
        price = 42
    elif sport.lower() == "boxing":
        price = 41
    elif sport.lower() == "yoga":
        price = 45
    elif sport.lower() == "zumba":
        price = 34
    elif sport.lower() == "dances":
        price = 51
    elif sport.lower() == "pilates":
        price = 39
elif gender.lower() == "f":
    if sport.lower() == "gym":
        price = 35
    elif sport.lower() == "boxing":
        price = 37
    elif sport.lower() == "yoga":
        price = 42
    elif sport.lower() == "zumba":
        price = 31
    elif sport.lower() == "dances":
        price = 53
    elif sport.lower() == "pilates":
        price = 37

if age <= 19:
    price *= 0.80

if available_money >= price:
    print(f"You purchased a 1 month pass for {sport.capitalize()}.")
else:
    difference = abs(price - available_money)
    print(f"You don't have enough money! You need ${difference:.2f} more.")
