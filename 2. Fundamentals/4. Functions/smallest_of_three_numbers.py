def smallest_number_finder(num1, num2, num3):
    smallest_number = min(num1, num2, num3)
    return smallest_number


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(smallest_number_finder(first_number, second_number, third_number))
