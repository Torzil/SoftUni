tournaments_number = int(input())
starting_points = int(input())

final_points = 0
tournament_wins = 0

for tournament in range(tournaments_number):
    finishing_place = input()
    if finishing_place == "W":
        final_points += 2000
        tournament_wins += 1
    elif finishing_place == "F":
        final_points += 1200
    elif finishing_place == "SF":
        final_points += 720

wins_percentage = tournament_wins / tournaments_number * 100
average_points = final_points // tournaments_number
final_points += starting_points

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{wins_percentage:.2f}%")
