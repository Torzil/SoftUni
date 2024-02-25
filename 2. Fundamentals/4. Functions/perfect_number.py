def perfect_number_finder(num):
    proper_divisor_sum = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            proper_divisor_sum += divisor
    if num == proper_divisor_sum:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())

print(perfect_number_finder(number))
