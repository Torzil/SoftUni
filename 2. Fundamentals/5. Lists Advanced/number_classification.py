def positive_numbers(nums_list):
    positive_numbers_list = [num for num in nums_list if num >= 0]
    positive_nums = ", ".join(map(str, positive_numbers_list))
    return positive_nums


def negative_numbers(nums_list):
    negative_numbers_list = [num for num in nums_list if num < 0]
    positive_nums = ", ".join(map(str, negative_numbers_list))
    return positive_nums


def even_numbers(nums_list):
    even_numbers_list = [num for num in nums_list if num % 2 == 0]
    positive_nums = ", ".join(map(str, even_numbers_list))
    return positive_nums


def odd_numbers(nums_list):
    odd_numbers_list = [num for num in nums_list if num % 2 != 0]
    positive_nums = ", ".join(map(str, odd_numbers_list))
    return positive_nums


numbers_list = [int(num) for num in input().split(", ")]
print(f"Positive: {positive_numbers(numbers_list)}")
print(f"Negative: {negative_numbers(numbers_list)}")
print(f"Even: {even_numbers(numbers_list)}")
print(f"Odd: {odd_numbers(numbers_list)}")
