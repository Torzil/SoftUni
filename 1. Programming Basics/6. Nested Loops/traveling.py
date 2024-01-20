destination = input()
while destination != "End":
    saved_money = 0
    needed_money = float(input())
    while saved_money < needed_money:
        savings = float(input())
        saved_money += savings
        if saved_money >= needed_money:
            print(f"Going to {destination}!")
            break
    destination = input()
