available_dog_food = int(input())
food_is_enough = True

available_dog_food *= 1000

food_eaten = input()
while food_eaten != "Adopted":
    available_dog_food -= int(food_eaten)
    if available_dog_food < 0:
        food_is_enough = False
    food_eaten = input()

difference = abs(available_dog_food)

if food_is_enough:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")
