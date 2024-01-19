chrysanthemums_number = int(input())
roses_number = int(input())
tulips_number = int(input())
season = input()
day_is_holiday = input()

chrysanthemum_price = 0
rose_price = 0
tulip_price = 0
total_price = 0

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2.00
    rose_price = 4.10
    tulip_price = 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    rose_price = 4.50
    tulip_price = 4.15

total_price = chrysanthemums_number * chrysanthemum_price\
    + roses_number * rose_price + tulips_number * tulip_price

if day_is_holiday == "Y":
    total_price *= 1.15

if tulips_number > 7 and season == "Spring":
    total_price *= 0.95
if roses_number >= 10 and season == "Winter":
    total_price *= 0.90
if (chrysanthemums_number + roses_number + tulips_number) > 20:
    total_price *= 0.80

total_price += 2

print(f"{total_price:.2f}")
