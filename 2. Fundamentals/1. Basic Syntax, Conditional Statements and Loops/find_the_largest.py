# number = list(input())
# 
# number.sort(reverse=True)
# 
# biggest_number = "".join(number)
# 
# print(biggest_number)

number = input()
for n in range(9, -1, -1):
    for i in number:
        if int(i) == int(n):
            print(n, end="")
