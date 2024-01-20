number_of_pairs = int(input())
biggest_difference = 0
pair_value_1 = int(input()) + int(input())

for pair in range(number_of_pairs - 1):
    pair_value_2 = int(input()) + int(input())
    difference = abs(pair_value_1 - pair_value_2)
    if difference > biggest_difference:
        biggest_difference = difference
    pair_value_1 = pair_value_2
if biggest_difference == 0:
    print(f"Yes, value={pair_value_1}")
else:
    print(f"No, maxdiff={biggest_difference}")
