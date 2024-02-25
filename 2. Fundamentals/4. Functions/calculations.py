def multiplication(a, b):
    return a * b


def division(a, b):
    return a // b


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


operator = input()
first_num = int(input())
second_num = int(input())


def calculation(operation):
    if operation == "multiply":
        return multiplication(first_num, second_num)
    elif operation == "divide":
        if second_num != 0:
            return division(first_num, second_num)
        else:
            return "Cannot divide by zero!"
    elif operation == "add":
        return addition(first_num, second_num)
    elif operation == "subtract":
        return subtraction(first_num, second_num)


print(calculation(operator))
