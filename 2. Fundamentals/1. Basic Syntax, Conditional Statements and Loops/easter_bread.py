budget = float(input())
flour_price = float(input())
eggs_price = flour_price * 0.75
liter_milk_price = flour_price * 1.25
quarter_milk_price = liter_milk_price / 4

loaf_price = flour_price + eggs_price + quarter_milk_price
max_loafs = int(budget // loaf_price)
leftover_money = budget - max_loafs * loaf_price

total_colored_eggs = 0
for current_loaf in range(1, max_loafs + 1):
    total_colored_eggs += 3
    if current_loaf % 3 == 0:
        total_colored_eggs -= current_loaf - 2

print(f"You made {max_loafs} loaves of Easter bread! Now you have {total_colored_eggs} eggs and {leftover_money:.2f}BGN left.")
