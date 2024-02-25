def sum_numbers(num1, num2):
    return num1 + num2


def subtract(addition_sum, num3):
    return addition_sum - num3


def add_and_subtract(num1, num2, num3):
    addition_result = sum_numbers(first_number, second_number)
    subtraction_result = subtract(addition_result, third_number)
    return subtraction_result


first_number, second_number, third_number = int(input()), int(input()), int(input())

print(add_and_subtract(first_number, second_number, third_number))
