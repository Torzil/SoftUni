cake_length = int(input())
cake_width = int(input())
total_cake_pieces = cake_length * cake_width
cake_is_finished = False

command = input()
while command != "STOP":
    total_cake_pieces -= int(command)
    if total_cake_pieces <= 0:
        cake_is_finished = True
        break

    command = input()

if cake_is_finished:
    difference = abs(total_cake_pieces)
    print(f"No more cake left! You need {difference} pieces more.")
else:
    print(f"{total_cake_pieces} pieces are left.")
