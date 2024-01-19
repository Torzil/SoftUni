season = input()
kilometers_per_month = float(input())
price_per_kilometer = 0

if kilometers_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_kilometer = 0.75
    elif season == "Summer":
        price_per_kilometer = 0.90
    elif season == "Winter":
        price_per_kilometer = 1.05
elif kilometers_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_kilometer = 0.95
    elif season == "Summer":
        price_per_kilometer = 1.10
    elif season == "Winter":
        price_per_kilometer = 1.25
elif kilometers_per_month <= 20000:
    price_per_kilometer = 1.45

season_salary = kilometers_per_month * 4 * price_per_kilometer * 0.90

print(f"{season_salary:.2f}")
