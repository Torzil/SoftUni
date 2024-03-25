stock = {}

while True:
    command = input().split()

    if command[0] == "statistics":
        break

    if command[0] not in stock.keys():
        stock.update({command[0]: int(command[1])})
    else:
        stock[command[0]] += int(command[1])

print("Products in stock:")
for key, value in stock.items():
    print(f"- {key} {value}")

print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")
