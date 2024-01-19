number_of_floors = int(input())
rooms_per_floor = int(input())
room_type = ""

for floor in range(number_of_floors, 0, -1):
    for room in range(rooms_per_floor):
        if floor % 2 == 0:
            room_type = "O"
        else:
            room_type = "A"
        if floor == number_of_floors:
            room_type = "L"
        print(f"{room_type}{floor}{room}", end=" ")
    print()
