movie_name = input()
projection_days = int(input())
daily_tickets_sold = int(input())
ticket_price = float(input())
studio_fee_percent = int(input())

gross_profits = daily_tickets_sold * ticket_price * projection_days
total_studio_fee = gross_profits * (studio_fee_percent / 100)
net_profits = gross_profits - total_studio_fee

print(f"The profit from the movie {movie_name} is {net_profits:.2f} lv.")
