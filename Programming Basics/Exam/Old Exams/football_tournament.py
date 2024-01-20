team_name = input()
current_season_matches = int(input())
number_of_W = 0
number_of_D = 0
number_of_L = 0
total_season_points = 0

if current_season_matches == 0:
    print(f"{team_name} hasn't played any games during this season.")
    exit()

for match in range(current_season_matches):
    match_result = input()
    if match_result == "W":
        number_of_W += 1
        total_season_points += 3
    elif match_result == "D":
        number_of_D += 1
        total_season_points += 1
    elif match_result == "L":
        number_of_L += 1

win_rate = number_of_W / current_season_matches * 100

print(f"{team_name} has won {total_season_points} points during this season.")
print("Total stats:")
print(f"## W: {number_of_W}")
print(f"## D: {number_of_D}")
print(f"## L: {number_of_L}")
print(f"Win rate: {win_rate:.2f}%")
