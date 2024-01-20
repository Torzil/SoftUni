budget = float(input())
season = input()
country = ""
accommodation = ""
total_price = 0

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        country = "Alaska"
        total_price = budget * 0.65
    elif season == "Winter":
        country = "Morocco"
        total_price = budget * 0.45
elif budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        country = "Alaska"
        total_price = budget * 0.80
    elif season == "Winter":
        country = "Morocco"
        total_price = budget * 0.60
elif budget > 3000:
    accommodation = "Hotel"
    total_price = budget * 0.90
    if season == "Summer":
        country = "Alaska"
    elif season == "Winter":
        country = "Morocco"

print(f"{country} - {accommodation} - {total_price:.2f}")
