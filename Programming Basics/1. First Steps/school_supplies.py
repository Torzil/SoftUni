number_of_pens = int(input())
number_of_markers = int(input())
liters_of_detergent = int(input())
discount_percent = int(input())

pens_price = 5.80
markers_price = 7.20
detergent_price = 1.20

sum = number_of_pens * pens_price \
       + number_of_markers * markers_price \
       + liters_of_detergent * detergent_price
final_sum = sum - (sum * discount_percent / 100)

print(final_sum)