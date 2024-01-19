airline_name = input()
adult_tickets_number = int(input())
child_tickets_number = int(input())
adult_ticket_net_price = float(input())
service_fee = float(input())

child_ticket_net_price = adult_ticket_net_price * 0.3
total_sum = (adult_tickets_number * adult_ticket_net_price) + (adult_tickets_number * service_fee) \
            + (child_tickets_number * child_ticket_net_price) + (child_tickets_number * service_fee)
agency_profit = total_sum * 0.2
agency_profit = format(agency_profit, '.2f')

print(f"The profit of your agency from {airline_name} tickets is {agency_profit} lv.")
