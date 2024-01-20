user_number = int(input())
combination_counter = 0
for x in range(user_number + 1):
    for y in range(user_number + 1):
        for z in range(user_number + 1):
            if x + y + z == user_number:
                combination_counter += 1

print(combination_counter)
