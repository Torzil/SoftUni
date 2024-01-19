actor_name = input()
academy_points = float(input())
number_of_judges = int(input())
actor_points = academy_points
actor_is_nominated = False

for judge in range(number_of_judges):
    judge_name = input()
    judge_points = float(input())
    actor_points += len(judge_name) * judge_points / 2
    if actor_points > 1250.5:
        actor_is_nominated = True
        break

needed_points = 1250.5 - actor_points

if actor_is_nominated:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
