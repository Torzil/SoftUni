from math import ceil

name_of_series = input()
episode_duration = int(input())
break_duration = int(input())

lunch_duration = break_duration / 8
relaxation_duration = break_duration / 4

needed_time = episode_duration + lunch_duration + relaxation_duration

difference = abs(break_duration - needed_time)
difference = ceil(difference)

if needed_time <= break_duration:
    print(f"You have enough time to watch {name_of_series} and left \
with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_series}, \
you need {difference} more minutes.")
