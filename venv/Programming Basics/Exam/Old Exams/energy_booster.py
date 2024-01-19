fruit_type = input()
package_size = input()
number_of_packages = int(input())
price_per_piece = 0

if package_size.lower() == "small":
    package_size = 2
    if fruit_type.lower() == "watermelon":
        price_per_piece = 56
    elif fruit_type.lower() == "mango":
        price_per_piece = 36.66
    elif fruit_type.lower() == "pineapple":
        price_per_piece = 42.10
    elif fruit_type.lower() == "raspberry":
        price_per_piece = 20
elif package_size.lower() == "big":
    package_size = 5
    if fruit_type.lower() == "watermelon":
        price_per_piece = 28.70
    elif fruit_type.lower() == "mango":
        price_per_piece = 19.60
    elif fruit_type.lower() == "pineapple":
        price_per_piece = 24.80
    elif fruit_type.lower() == "raspberry":
        price_per_piece = 15.20

total_price = package_size * price_per_piece * number_of_packages

if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.5

print(f"{total_price:.2f} lv.")
