number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
number_4 = int(number_3 / 2)

for num1 in range(number_1, number_2):
    for num2 in range(1, number_3):
        for num3 in range(1, number_4):
            if num1 % 2 == 1 and ((num2 + num3 + num1) % 2 == 1):
                print(f"{chr(num1)}-{num2}{num3}{num1}")
