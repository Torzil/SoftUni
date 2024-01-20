number_of_turns = int(input())
total_points = 0
points_between_0_9 = 0
points_between_10_19 = 0
points_between_20_29 = 0
points_between_30_39 = 0
points_between_40_50 = 0
invalid_numbers = 0

for turn in range(number_of_turns):
    current_points = int(input())
    if current_points < 0 or current_points > 50:
        invalid_numbers += 1
        total_points /= 2
    elif current_points < 10:
        points_between_0_9 += 1
        total_points += current_points * 0.2
    elif current_points < 20:
        points_between_10_19 += 1
        total_points += current_points * 0.3
    elif current_points < 30:
        points_between_20_29 += 1
        total_points += current_points * 0.4
    elif current_points < 40:
        points_between_30_39 += 1
        total_points += 50
    elif current_points <= 50:
        points_between_40_50 += 1
        total_points += 100

percentage_points_between_0_9 = points_between_0_9 / number_of_turns * 100
percentage_points_between_10_19 = points_between_10_19 / number_of_turns * 100
percentage_points_between_20_29 = points_between_20_29 / number_of_turns * 100
percentage_points_between_30_39 = points_between_30_39 / number_of_turns * 100
percentage_points_between_40_50 = points_between_40_50 / number_of_turns * 100
percentage_invalid_numbers = invalid_numbers / number_of_turns * 100

print(f"{total_points:.2f}")
print(f"From 0 to 9: {percentage_points_between_0_9:.2f}%")
print(f"From 10 to 19: {percentage_points_between_10_19:.2f}%")
print(f"From 20 to 29: {percentage_points_between_20_29:.2f}%")
print(f"From 30 to 39: {percentage_points_between_30_39:.2f}%")
print(f"From 40 to 50: {percentage_points_between_40_50:.2f}%")
print(f"Invalid numbers: {percentage_invalid_numbers:.2f}%")
