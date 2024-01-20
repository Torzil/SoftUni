season = input()
group_type = input()
students_number = int(input())
nights_number = int(input())
price_per_night = 0
total_price = 0
sport = ""

if season == "Winter":
    if group_type == "boys":
        price_per_night = 9.60
        sport = "Judo"
    elif group_type == "girls":
        price_per_night = 9.60
        sport = "Gymnastics"
    elif group_type == "mixed":
        price_per_night = 10
        sport = "Ski"
elif season == "Spring":
    if group_type == "boys":
        price_per_night = 7.20
        sport = "Tennis"
    elif group_type == "girls":
        price_per_night = 7.20
        sport = "Athletics"
    elif group_type == "mixed":
        price_per_night = 9.50
        sport = "Cycling"
elif season == "Summer":
    if group_type == "boys":
        price_per_night = 15
        sport = "Football"
    elif group_type == "girls":
        price_per_night = 15
        sport = "Volleyball"
    elif group_type == "mixed":
        price_per_night = 20
        sport = "Swimming"

total_price = nights_number * price_per_night * students_number

if students_number >= 50:
    total_price *= 0.5
elif students_number >= 20:
    total_price *= 0.85
elif students_number >= 10:
    total_price *= 0.95

print(f"{sport} {total_price:.2f} lv.")
