pinnacle = int(input())

for i in range(1, pinnacle + 1):
    for j in range(0, i):
        print('*', end='')
    print()
for i in range(pinnacle - 1, 0, -1):
    for j in range(0, i):
        print('*', end='')
    print()
