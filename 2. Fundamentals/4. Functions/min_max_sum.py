def min_max_sum(lst):
    min_number = min(lst)
    max_number = max(lst)
    sum_numbers = sum(lst)
    return print(f"The minimum number is {min_number}\n"
                 f"The maximum number is {max_number}\n"
                 f"The sum number is: {sum_numbers}")


numbers = [int(num) for num in input().split()]
min_max_sum(numbers)
