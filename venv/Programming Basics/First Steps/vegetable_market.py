vegetables_price = float(input())
fruit_price = float(input())
vegetables_kilograms = int(input())
fruit_kilograms = int(input())

total_amount_bgn = vegetables_price * vegetables_kilograms \
    + fruit_price * fruit_kilograms
total_amount_eur = total_amount_bgn * 0.51546392

print (format(total_amount_eur, '.2f'))