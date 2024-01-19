party_price = float(input())
love_letters_number = int(input())
wax_roses_number = int(input())
keychains_number = int(input())
caricatures_number = int(input())
surprise_fortunes_number = int(input())

love_letter_price = 0.60
wax_rose_price = 7.20
keychain_price = 3.60
caricature_price = 18.20
surprise_fortune_price = 22

total_items_ordered = love_letters_number + wax_roses_number\
    + keychains_number + caricatures_number + surprise_fortunes_number

gross_sum = love_letters_number * love_letter_price + wax_roses_number * wax_rose_price\
    + keychains_number * keychain_price + caricatures_number * caricature_price\
    + surprise_fortunes_number * surprise_fortune_price

if total_items_ordered >= 25:
    gross_sum *= 0.65

net_sum = gross_sum * 0.9

difference = abs(party_price - net_sum)

if net_sum >= party_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
