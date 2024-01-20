budget = float(input())
ticket_category = input()
people_in_group = int(input())

ticket_price = 0
transport_cost = 0
total_ticket_price = 0
total_group_cost = 0

if people_in_group < 5:
    transport_cost = budget * 0.75
elif people_in_group < 10:
    transport_cost = budget * 0.60
elif people_in_group < 25:
    transport_cost = budget * 0.50
elif people_in_group < 50:
    transport_cost = budget * 0.40
elif people_in_group >= 50:
    transport_cost = budget * 0.25

if ticket_category == "VIP":
    ticket_price = 499.99
elif ticket_category == "Normal":
    ticket_price = 249.99

total_ticket_cost = people_in_group * ticket_price
total_group_cost = transport_cost + total_ticket_cost
difference = abs(budget - total_group_cost)

if budget >= total_group_cost:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
