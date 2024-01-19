player_has_made_hat_trick = False
best_player = ""
best_player_goals = 0
current_player_goals = 0

current_player_name = input()
while current_player_name != "END":
    number_of_goals = int(input())
    if number_of_goals > current_player_goals:
        best_player = current_player_name
        best_player_goals = number_of_goals
    current_player_goals = number_of_goals
    if current_player_goals >= 3:
        player_has_made_hat_trick = True
    if current_player_goals >= 10:
        best_player = current_player_name
        best_player_goals = current_player_goals
        break

    current_player_name = input()

print(f"{best_player} is the best player!")
if player_has_made_hat_trick:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_goals} goals.")
