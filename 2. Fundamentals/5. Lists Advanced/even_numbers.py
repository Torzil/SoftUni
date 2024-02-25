numbers_list = [int(number) for number in input().split(", ")]
index_list = []
for index, item in enumerate(numbers_list):
    if item % 2 == 0:
        index_list.append(index)

print(index_list)
