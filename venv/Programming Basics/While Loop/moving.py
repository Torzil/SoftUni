apartment_width = int(input())
apartment_length = int(input())
apartment_height = int(input())
apartment_volume = apartment_width * apartment_length * apartment_height
apartment_is_full = False

command = input()
while command != "Done":
    command = int(command)
    apartment_volume -= command
    if apartment_volume <= 0:
        apartment_is_full = True
        break

    command = input()

difference = abs(apartment_volume)

if apartment_is_full:
    print(f"No more free space! You need {difference} Cubic meters more.")
else:
    print(f"{difference} Cubic meters left.")
