minutes_per_walk = int(input())
walks_per_day = int(input())
cat_consumed_calories = int(input())

total_burned_calories = walks_per_day * minutes_per_walk * 5

if total_burned_calories >= cat_consumed_calories * 0.5:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burned_calories}.")
