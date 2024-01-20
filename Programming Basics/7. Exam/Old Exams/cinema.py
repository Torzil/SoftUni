theater_places = int(input())
moviegoers = 0
total_profit = 0
theater_is_full = False

command = input()
while command != "Movie time!":
    command = int(command)
    moviegoers += command
    if moviegoers > theater_places:
        theater_is_full = True
        break
    current_price = command * 5
    if command % 3 == 0:
        current_price -= 5
    total_profit += current_price
    command = input()

if theater_is_full:
    print("The cinema is full.")
else:
    difference = theater_places - moviegoers
    print(f"There are {difference} seats left in the cinema.")

print(f"Cinema income - {total_profit} lv.")
