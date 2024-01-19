month = input()
nights_stayed = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if nights_stayed > 14:
        studio_price *= 0.7
    elif nights_stayed > 7:
        studio_price *= 0.95
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if nights_stayed > 14:
        studio_price *= 0.8
elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77

if nights_stayed > 14:
    apartment_price *= 0.9

studio_total_price = nights_stayed * studio_price
apartment_total_price = nights_stayed * apartment_price

print(f"Apartment: {apartment_total_price:.2f} lv.")
print(f"Studio: {studio_total_price:.2f} lv.")
