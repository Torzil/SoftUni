start_number = int(input())
end_number = int(input())

for number in range(start_number, end_number + 1):
    odd_sum = 0
    even_sum = 0
    for index, decimal in enumerate(str(number)):
        if index % 2 == 0:
            odd_sum += int(decimal)
        else:
            even_sum += int(decimal)
    if odd_sum == even_sum:
        print(number, end=" ")
