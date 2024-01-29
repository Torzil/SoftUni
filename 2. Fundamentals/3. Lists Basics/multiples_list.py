factor = int(input())
count = int(input())

numbers_list = []

for number in range(1, count + 1):
    numbers_list.append(number * factor)

print(numbers_list)
