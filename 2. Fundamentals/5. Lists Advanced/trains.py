train_wagons = [0] * int(input())


def train_command():
    while True:
        command = input().split()

        if command[0] == "End":
            break

        elif command[0] == "add":
            train_wagons[-1] += int(command[1])

        elif command[0] == "insert":
            index = int(command[1])
            train_wagons[index] += int(command[2])

        elif command[0] == "leave":
            index = int(command[1])
            train_wagons[index] -= int(command[2])

    return train_wagons


print(train_command())
