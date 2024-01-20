distance = int(input())
time_of_day = (input())
price = 0

if distance >= 100:
    price = distance * 0.06
elif distance >= 20:
    price = distance * 0.09
elif distance < 20:
    price = 0.70
    if time_of_day == "day":
        price += distance * 0.79
    if time_of_day == "night":
        price += distance * 0.90

print(f"{price:.2f}")
