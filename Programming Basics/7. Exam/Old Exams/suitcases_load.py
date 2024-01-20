plane_baggage_space = float(input())
there_is_space_left = True
total_suitcases_loaded = 0

current_suitcase_volume = input()
while current_suitcase_volume != "End":
    current_suitcase_volume = float(current_suitcase_volume)
    total_suitcases_loaded += 1
    if total_suitcases_loaded % 3 == 0:
        current_suitcase_volume *= 1.1
    plane_baggage_space -= current_suitcase_volume
    if plane_baggage_space < 0:
        total_suitcases_loaded -= 1
        there_is_space_left = False
        break
    current_suitcase_volume = str(input())

if there_is_space_left:
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")
print(f"Statistic: {total_suitcases_loaded} suitcases loaded.")
