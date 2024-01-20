number = int(input())
end_is_reached = False
number_counter = 1

for row in range(1, number + 1):
    for column in range(1, row + 1):
        if number_counter > number:
            end_is_reached = True
            break
        print(number_counter, end=" ")
        number_counter += 1
    if end_is_reached:
        break
    print()
