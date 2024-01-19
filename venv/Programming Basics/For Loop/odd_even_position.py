from math import inf
numbers_count = int(input())
odd_min = inf
odd_max = -inf
odd_sum = 0
even_min = inf
even_max = -inf
even_sum = 0

for number in range(1, numbers_count + 1):
    current_number = float(input())
    if number % 2 == 0:
        even_sum += current_number
        if current_number > even_max:
            even_max = current_number
        if current_number < even_min:
            even_min = current_number
    else:
        odd_sum += current_number
        if current_number > odd_max:
            odd_max = current_number
        if current_number < odd_min:
            odd_min = current_number

if odd_min == inf and odd_max == -inf:
    odd_min = "No"
    odd_max = "No"
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min},")
    print(f"OddMax={odd_max},")
else:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
if even_min == inf and even_max == -inf:
    even_min = "No"
    even_max = "No"
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min},")
    print(f"EvenMax={even_max}")
else:
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
