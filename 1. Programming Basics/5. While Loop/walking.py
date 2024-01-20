target_steps = 10000
total_steps = 0
final_steps = 0
goal_is_reached = False

action = input()
while not goal_is_reached:
    if action == "Going home":
        final_steps = int(input())
        total_steps += final_steps
        break
    action = int(action)
    total_steps += action
    if total_steps >= target_steps:
        goal_is_reached = True
        if goal_is_reached:
            break
    action = input()

difference = abs(target_steps - total_steps)

if total_steps >= target_steps:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")
