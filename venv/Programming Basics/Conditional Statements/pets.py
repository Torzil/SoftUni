from math import ceil, floor

number_of_days = int(input())
kilograms_of_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

dog_food_needed = number_of_days * dog_food_per_day
cat_food_needed = number_of_days * cat_food_per_day
turtle_food_needed = number_of_days * (turtle_food_per_day * 0.001)
total_food_needed = dog_food_needed + cat_food_needed + turtle_food_needed

difference = abs(kilograms_of_food - total_food_needed)

if total_food_needed <= kilograms_of_food:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")
