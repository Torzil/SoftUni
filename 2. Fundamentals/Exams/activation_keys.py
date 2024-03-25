key = input()

while True:
    command = input()

    if command == "Generate":
        break

    command = command.split(">>>")
    action = command[0]

    if action == "Contains":
        substring = command[1]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        flip_type = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        substring = ""
        if flip_type == "Lower":
            substring = key[start_index:end_index].lower()
        elif flip_type == "Upper":
            substring = key[start_index:end_index].upper()
        key = key[:start_index] + substring + key[end_index:]
        print(key)

    elif action == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        key = key[:start_index] + key[end_index:]
        print(key)

print(f"Your activation key is: {key}")
