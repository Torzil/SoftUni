number_of_commands = int(input())
registered_users = {}


def register(user, number):
    if user not in registered_users:
        registered_users[user] = number
        return f"{user} registered {number} successfully"
    return f"ERROR: already registered with plate number {registered_users[user]}"


def unregister(user):
    if user in registered_users:
        del registered_users[user]
        return f"{user} unregistered successfully"
    return f"ERROR: user {user} not found"


for _ in range(number_of_commands):
    command = input().split()
    task = command[0]
    username = command[1]
    if len(command) == 3:
        plate_number = command[2]

    if task == "register":
        print(register(username, plate_number))
    elif task == "unregister":
        print(unregister(username))

for users, numbers in registered_users.items():
    print(f"{users} => {numbers}")
