number_of_men = int(input())
number_of_women = int(input())
max_tables = int(input())


for man in range(1, number_of_men + 1):
    for woman in range(1, number_of_women + 1):
        print(f"({man} <-> {woman})", end=" ")
        max_tables -= 1
        if max_tables <= 0:
            break
    if max_tables <= 0:
        break
