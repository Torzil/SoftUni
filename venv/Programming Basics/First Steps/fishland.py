mackerel_price = float(input())
sprat_price = float(input())
bonito_kilograms = float(input())
safrid_kilograms = float(input())
mussels_kilograms = int(input())

bonito_price = mackerel_price * 1.6
safrid_price = sprat_price * 1.8
mussels_price = 7.50

total_amount = bonito_price * bonito_kilograms \
    + safrid_price * safrid_kilograms \
    + mussels_price * mussels_kilograms

print (format(total_amount, '.2f'))