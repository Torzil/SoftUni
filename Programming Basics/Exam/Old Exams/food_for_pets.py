number_of_days = int(input())
total_food_amount = float(input())
total_food_eaten = 0
total_dog_food_eaten = 0
total_cat_food_eaten = 0
days_passed = 0
biscuits_given = 0

for day in range(number_of_days):
    days_passed += 1
    dog_food_eaten = int(input())
    total_dog_food_eaten += dog_food_eaten
    cat_food_eaten = int(input())
    total_cat_food_eaten += cat_food_eaten
    total_food_eaten += dog_food_eaten + cat_food_eaten
    if days_passed % 3 == 0:
        biscuits_given += (dog_food_eaten + cat_food_eaten) * 0.10

percent_total_dog_food_eaten = total_dog_food_eaten / total_food_eaten * 100
percent_total_cat_food_eaten = total_cat_food_eaten / total_food_eaten * 100
percent_total_food_eaten = total_food_eaten / total_food_amount * 100

print(f"Total eaten biscuits: {round(biscuits_given)}gr.")
print(f"{percent_total_food_eaten:.2f}% of the food has been eaten.")
print(f"{percent_total_dog_food_eaten:.2f}% eaten from the dog.")
print(f"{percent_total_cat_food_eaten:.2f}% eaten from the cat.")
