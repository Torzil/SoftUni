budget = int(input())

total_bill = 0

item_price = input()
while item_price != "End":
    total_bill += int(item_price)
    if total_bill > budget:
        print("You went in overdraft!")
        break
    item_price = input()
else:
    print("You bought everything needed.")
