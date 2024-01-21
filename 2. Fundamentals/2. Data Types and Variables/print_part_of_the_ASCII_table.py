range_start = int(input())
range_end = int(input())

for character in range(range_start, range_end + 1):
    if character == range_end:
        print(chr(character), end="")
    else:
        print(chr(character), end=" ")
