tournament_days = int(input())
total_wins = 0
total_losses = 0
total_funds = 0

for day in range(tournament_days):
    day_wins = 0
    day_losses = 0
    day_funds = 0
    sport = input()
    while sport != "Finish":
        result = input()
        if result == "win":
            day_wins += 1
            total_wins += 1
            day_funds += 20
        elif result == "lose":
            day_losses += 1
            total_losses += 1
        sport = input()
    if day_wins > day_losses:
        day_funds *= 1.1
    total_funds += day_funds

if total_wins > total_losses:
    total_funds *= 1.2
    print(f"You won the tournament! Total raised money: {total_funds:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_funds:.2f}")
