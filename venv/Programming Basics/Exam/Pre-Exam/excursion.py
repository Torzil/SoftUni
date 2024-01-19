people_in_group = int(input())
number_of_nights = int(input())
number_of_transport_cards = int(input())
number_of_museum_tickets = int(input())

price_per_night = 20
transport_card_price = 1.60
museum_ticket_price = 6

total_sum = (number_of_nights * price_per_night
             + number_of_transport_cards * transport_card_price
             + number_of_museum_tickets * museum_ticket_price) * people_in_group
total_sum += total_sum * 0.25

print(f"{total_sum:.2f}")
