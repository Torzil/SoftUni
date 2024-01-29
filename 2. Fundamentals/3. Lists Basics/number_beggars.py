numbers = input().split(", ")
beggars = int(input())
collected_numbers = []
starting_index = 0

for beggar in range(beggars):
    current_beggar_sum = 0
    for index in range(starting_index, len(numbers), beggars):
        current_beggar_sum += int(numbers[index])
    collected_numbers.append(current_beggar_sum)
    starting_index += 1

print(collected_numbers)
