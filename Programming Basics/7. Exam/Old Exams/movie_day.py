max_filming_time = int(input())
number_of_scenes = int(input())
time_per_scene = int(input())

prep_time = max_filming_time * 0.15
total_filming_time = number_of_scenes * time_per_scene + prep_time

difference = round(abs(max_filming_time - total_filming_time))

if total_filming_time <= max_filming_time:
    print(f"You managed to finish the movie on time! You have {difference} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {difference} minutes.")
