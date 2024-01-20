movie_name = input()
package_type = input()
number_of_tickets = int(input())
package_price = 0

if package_type == "Drink":
    if movie_name == "John Wick":
        package_price = 12
    elif movie_name == "Star Wars":
        package_price = 18
    elif movie_name == "Jumanji":
        package_price = 9
elif package_type == "Popcorn":
    if movie_name == "John Wick":
        package_price = 15
    elif movie_name == "Star Wars":
        package_price = 25
    elif movie_name == "Jumanji":
        package_price = 11
elif package_type == "Menu":
    if movie_name == "John Wick":
        package_price = 19
    elif movie_name == "Star Wars":
        package_price = 30
    elif movie_name == "Jumanji":
        package_price = 14

total_price = package_price * number_of_tickets

if movie_name == "Star Wars" and number_of_tickets >= 4:
    total_price *= 0.7
elif movie_name == "Jumanji" and number_of_tickets == 2:
    total_price *= 0.85

print(f"Your bill is {total_price:.2f} leva.")
