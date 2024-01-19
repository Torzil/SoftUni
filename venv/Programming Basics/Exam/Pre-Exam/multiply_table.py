input_number = input()

first_number = int(input_number[2])
second_number = int(input_number[1])
third_number = int(input_number[0])

for num1 in range(1, first_number + 1):
    for num2 in range(1, second_number + 1):
        for num3 in range(1, third_number + 1):
            result = num1 * num2 * num3
            print(f"{num1} * {num2} * {num3} = {result};")
