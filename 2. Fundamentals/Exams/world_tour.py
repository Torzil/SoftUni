travel_route = input()

while True:
    command = input()

    if command == "Travel":
        break

    command = command.split(":")

    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(travel_route):
            travel_route = travel_route[:index] + string + travel_route[index:]
        print(travel_route)

    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(travel_route) and 0 <= end_index < len(travel_route):
            travel_route = travel_route[:start_index] + travel_route[end_index + 1:]
        print(travel_route)

    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        if old_string in travel_route:
            travel_route = travel_route.replace(old_string, new_string)
        print(travel_route)

print(f"Ready for world tour! Planned stops: {travel_route}")
