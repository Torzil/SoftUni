actors_budget = float(input())
total_expenses = 0

actor_name = input()
while actor_name != "ACTION":
    if len(actor_name) > 15:
        total_expenses += (actors_budget - total_expenses) * 0.2
    else:
        actor_pay = float(input())
        total_expenses += actor_pay
    if total_expenses > actors_budget:
        break
    actor_name = input()

difference = f"{abs(actors_budget - total_expenses):.2f}"

if total_expenses <= actors_budget:
    print(f"We are left with {difference} leva.")
else:
    print(f"We need {difference} leva for our actors.")
