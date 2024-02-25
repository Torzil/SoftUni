list_as_string = input().split()
list_as_int = list(map(int, list_as_string))
removal_count = int(input())

for removal in range(removal_count):
    list_as_int.remove(min(list_as_int))

for index in range(len(list_as_int)):
    if index == len(list_as_int) - 1:
        print(list_as_int[index])
    else:
        print(list_as_int[index], end=", ")
