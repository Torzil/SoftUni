first_range_end = int(input())
second_range_end = int(input())
third_range_end = int(input())
prime_numbers = [2, 3, 5, 7]

for num1 in range(1, first_range_end + 1):
    for num2 in range(1, second_range_end + 1):
        for num3 in range(1, third_range_end + 1):
            if (num1 % 2 == 0 and num3 % 2 == 0) and (num2 in prime_numbers):
                print(f"{num1} {num2} {num3}")
