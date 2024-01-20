from math import ceil, floor

number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_roses = int(input())
number_of_cacti = int(input())
gift_price = float(input())

magnolia_price = 3.25
hyacinth_price = 4
rose_price = 3.50
cactus_price = 8

gross_income = number_of_magnolias * magnolia_price\
    + number_of_hyacinths * hyacinth_price\
    + number_of_roses * rose_price\
    + number_of_cacti * cactus_price
net_income = gross_income - (gross_income * 0.05)

difference = abs(gift_price - net_income)

if gift_price <= net_income:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")
