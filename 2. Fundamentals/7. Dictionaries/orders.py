orders = {}

while True:
    command = input()

    if command == "buy":
        break

    product_list = command.split()

    product = product_list[0]
    p_price = float(product_list[1])
    p_quantity = int(product_list[2])

    if product not in orders:
        orders[product] = {"price": 0.0, "quantity": 0}
    orders[product]["quantity"] += p_quantity
    if orders[product]["price"] != p_price:
        orders[product]["price"] = p_price

for prod, info in orders.items():
    total_price = info["price"] * info["quantity"]
    print(f"{prod} -> {total_price:.2f}")
