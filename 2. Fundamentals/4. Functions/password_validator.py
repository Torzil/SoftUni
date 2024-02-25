def password_validator(password):
    password_is_valid = True
    digit_sum = 0
    for digit in password:
        if digit.isdigit():
            digit_sum += 1
    if not (6 <= len(password) <= 10):
        print("Password must be between 6 and 10 characters")
        password_is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        password_is_valid = False
    if digit_sum < 2:
        print("Password must have at least 2 digits")
        password_is_valid = False
    if password_is_valid:
        print("Password is valid")


user_password = input()

password_validator(user_password)
