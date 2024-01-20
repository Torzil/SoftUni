days_off = int(input())

work_days = 365 - days_off
play_time = work_days * 63 + days_off * 127
play_norm = 30000
difference = abs(play_norm - play_time)

hours = difference // 60
minutes = difference % 60

if play_norm >= play_time:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
