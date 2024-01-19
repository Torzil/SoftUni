day = input()

ticket_price = 12

if day.lower() == "wednesday" or day.lower() == "thursday":
    ticket_price += 2
elif day.lower() == "saturday" or day.lower() == "sunday":
    ticket_price += 4

print(ticket_price)
