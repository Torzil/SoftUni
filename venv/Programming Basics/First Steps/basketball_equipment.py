annual_fee = int(input())

sneakers_price = annual_fee * 0.6
outfit_price = sneakers_price * 0.8
ball_price = outfit_price * 0.25
accessories_price = ball_price * 0.2

total_price = annual_fee + sneakers_price \
    + outfit_price + ball_price + accessories_price

print (total_price)