actor_name = input()
academy_points = float(input())
number_of_judges = int(input())

for judge in range(number_of_judges):
    judge_name = input()
    initial_judge_points = float(input())
    final_judge_points = (len(judge_name) * initial_judge_points) / 2
    academy_points += final_judge_points
    if academy_points >= 1250.5:
        break

difference = 1250.5 - academy_points

if academy_points >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")
