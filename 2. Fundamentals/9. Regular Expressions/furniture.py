import re

regex = r">>([A-Za-z]+)<<(\d+[\.\d+]*)!(\d+)"
purchased_furniture = []
total_price = 0

while True:
    text = input()
    if text == "Purchase":
        break
    match = re.search(regex, text)
    if match:
        furniture, price, quantity = match.groups()
        purchased_furniture.append(furniture)
        total_price += float(price) * int(quantity)

print("Bought furniture:")
for furniture in purchased_furniture:
    print(furniture)
print(f"Total money spend: {total_price:.2f}")
