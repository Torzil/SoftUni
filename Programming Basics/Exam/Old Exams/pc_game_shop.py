total_games_sold = int(input())
hearthstone_sales = 0
fornite_sales = 0
overwatch_sales = 0
other_games_sales = 0

for game in range(total_games_sold):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone_sales += 1
    elif game_name == "Fornite":
        fornite_sales += 1
    elif game_name == "Overwatch":
        overwatch_sales += 1
    else:
        other_games_sales += 1

percent_hearthstone_sales = hearthstone_sales / total_games_sold * 100
percent_fornite_sales = fornite_sales / total_games_sold * 100
percent_overwatch_sales = overwatch_sales / total_games_sold * 100
percent_other_games_sales = other_games_sales / total_games_sold * 100

print(f"Hearthstone - {percent_hearthstone_sales:.2f}%")
print(f"Fornite - {percent_fornite_sales:.2f}%")
print(f"Overwatch - {percent_overwatch_sales:.2f}%")
print(f"Others - {percent_other_games_sales:.2f}%")
