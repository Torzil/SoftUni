number_of_lines = int(input())
tank_capacity = 255

for line in range(number_of_lines):
    current_liters = int(input())
    if tank_capacity - current_liters < 0:
        print("Insufficient capacity!")
        continue
    tank_capacity -= current_liters

liters_in_tank = 255 - tank_capacity

print(liters_in_tank)
