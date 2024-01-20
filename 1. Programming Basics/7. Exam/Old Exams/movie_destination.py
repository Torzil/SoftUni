budget = float(input())
destination = input()
season = input()
days = int(input())
price_per_day = 0

if season == "Winter":
    if destination == "Dubai":
        price_per_day = 45000
    elif destination == "Sofia":
        price_per_day = 17000
    elif destination == "London":
        price_per_day = 24000
elif season == "Summer":
    if destination == "Dubai":
        price_per_day = 40000
    elif destination == "Sofia":
        price_per_day = 12500
    elif destination == "London":
        price_per_day = 20250

total_price = price_per_day * days

if destination == "Dubai":
    total_price *= 0.7
elif destination == "Sofia":
    total_price *= 1.25

difference = f"{abs(budget - total_price):.2f}"

if total_price <= budget:
    print(f"The budget for the movie is enough! We have {difference} leva left!")
else:
    print(f"The director needs {difference} leva more!")
