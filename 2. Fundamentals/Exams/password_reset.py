password = input()

while True:
    command = input()

    if command == "Done":
        break

    command = command.split()
    action = command[0]

    if action == "TakeOdd":
        new_password = ""
        for index in range(len(password)):
            if index % 2 != 0:
                new_password += password[index]
        password = new_password
        print(password)

    elif action == "Cut":
        substring = ""
        index = int(command[1])
        length = int(command[2])

        substring += password[index:index+length]
        password = password.replace(substring, "", 1)
        print(password)

    elif action == "Substitute":
        substring = command[1]
        replacement = command[2]
        if substring in password:
            password = password.replace(substring, replacement)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")
