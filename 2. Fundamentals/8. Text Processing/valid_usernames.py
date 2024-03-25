usernames_list = input().split(", ")


def len_check(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def char_check(username):
    for char in username:
        if not char.isalnum():
            if not (char == "-" or char == "_"):
                return False
    return True


def space_check(username):
    if " " in username:
        return False
    return True


def username_validator(users_list):
    for username in users_list:
        if len_check(username) and char_check(username) and space_check(username):
            print(username)


username_validator(usernames_list)
