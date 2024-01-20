user_number = int(input())


for number in range(1111, 9999 + 1):
    division_counter = 0
    for index, decimal in enumerate(str(number)):
        if int(decimal) == 0:
            break
        if user_number % int(decimal) == 0:
            division_counter += 1
    if division_counter == 4:
        print(number, end=" ")
