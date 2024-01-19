needed_money = float(input())
current_funds = float(input())
days = 0
days_spending_counter = 0
spending_too_many_days_in_a_row = False

action = input()
while current_funds < needed_money:
    used_funds = float(input())
    days += 1
    if action == "spend":
        current_funds -= used_funds
        days_spending_counter += 1
        if current_funds < 0:
            current_funds = 0
        if days_spending_counter == 5:
            spending_too_many_days_in_a_row = True
            break
    if action == "save":
        days_spending_counter = 0
        current_funds += used_funds
        if current_funds >= needed_money:
            break
    action = input()
if spending_too_many_days_in_a_row:
    print("You can't save the money.")
    print(f"{days}")
else:
    print(f"You saved the money for {days} days.")
