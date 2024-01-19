days = int(input())
room_type = input()
rating = input()

room_for_one_person = 18.00
apartment = 25.00
president_apartment = 35.00
nights = days - 1
total_price = 0

if room_type == "room for one person":
    total_price = nights * room_for_one_person
elif room_type == "apartment":
    total_price = nights * apartment
    if nights < 10:
        total_price *= 0.7
    elif nights < 15:
        total_price *= 0.65
    elif nights > 15:
        total_price *= 0.5
elif room_type == "president apartment":
    total_price = nights * president_apartment
    if nights < 10:
        total_price *= 0.9
    elif nights < 15:
        total_price *= 0.85
    elif nights > 15:
        total_price *= 0.8

if rating == "positive":
    total_price *= 1.25
elif rating == "negative":
    total_price *= 0.9

print(f"{total_price:.2f}")
