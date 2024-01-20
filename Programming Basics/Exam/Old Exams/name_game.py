last_player_points = 0
best_player_name = ""
best_player_points = 0

player_name = input()
while player_name != "Stop":
    current_player_points = 0
    for letter in player_name:
        user_guess = int(input())
        check = ord(letter)
        if user_guess == check:
            current_player_points += 10
        else:
            current_player_points += 2
    if current_player_points >= best_player_points:
        best_player_name = player_name
        best_player_points = current_player_points
    last_player_points = current_player_points
    player_name = input()

print(f"The winner is {best_player_name} with {best_player_points} points!")
