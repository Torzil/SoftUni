budget = float(input())
season = input()

location = ""
accommodation = ""
accommodation_price = 0

if budget <= 100:
    location = "Bulgaria"
    if season.lower() == "summer":
        accommodation = "Camp"
        accommodation_price = budget * 0.3
    elif season.lower() == "winter":
        accommodation = "Hotel"
        accommodation_price = budget * 0.7
elif budget <= 1000:
    location = "Balkans"
    if season.lower() == "summer":
        accommodation = "Camp"
        accommodation_price = budget * 0.4
    elif season.lower() == "winter":
        accommodation = "Hotel"
        accommodation_price = budget * 0.8
elif budget > 1000:
    location = "Europe"
    accommodation = "Hotel"
    accommodation_price = budget * 0.9

print(f"Somewhere in {location}")
print(f"{accommodation} - {accommodation_price:.2f}")
