start_of_interval = int(input())
end_of_interval = int(input())
magic_number = int(input())
first_number = 0
second_number = 0
number_of_combinations = 0
combination_is_found = False

for first_number in range(start_of_interval, end_of_interval + 1):
    for second_number in range(start_of_interval, end_of_interval + 1):
        number_of_combinations += 1
        if first_number + second_number == magic_number:
            combination_is_found = True
            break
    if combination_is_found:
        break

if combination_is_found:
    print(f"Combination N:{number_of_combinations} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{number_of_combinations} combinations - neither equals {magic_number}")
