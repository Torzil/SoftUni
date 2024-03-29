message = input()

while True:
    command = input()
    if command == "Decode":
        break

    command = command.split("|")
    action = command[0]

    if action == "Move":
        number_of_letters = int(command[1])
        letters_to_move = message[:number_of_letters]
        message = message[number_of_letters:] + letters_to_move
    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index:]
    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")
