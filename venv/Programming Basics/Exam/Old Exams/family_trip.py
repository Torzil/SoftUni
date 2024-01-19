budget = float(input())
nights = int(input())
price_per_night = float(input())
additional_expenses_percent = int(input())

if nights > 7:
    price_per_night *= 0.95

total_price = nights * price_per_night + budget * (additional_expenses_percent / 100)

difference = abs(budget - total_price)

if budget >= total_price:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")
