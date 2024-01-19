junior_bikers_number = int(input())
senior_bikers_number = int(input())
track_type = input()

biker_type = ""
junior_ticket_price = 0
senior_ticket_price = 0

if track_type == "trail":
    junior_ticket_price = 5.50
    senior_ticket_price = 7
elif track_type == "cross-country":
    junior_ticket_price = 8
    senior_ticket_price = 9.50
    if junior_bikers_number + senior_bikers_number >= 50:
        junior_ticket_price *= 0.75
        senior_ticket_price *= 0.75
elif track_type == "downhill":
    junior_ticket_price = 12.25
    senior_ticket_price = 13.75
elif track_type == "road":
    junior_ticket_price = 20
    senior_ticket_price = 21.50

total_funds = (junior_bikers_number * junior_ticket_price
               + senior_bikers_number * senior_ticket_price) * 0.95

print(f"{total_funds:.2f}")
