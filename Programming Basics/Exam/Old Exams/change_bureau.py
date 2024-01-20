bitcoin_amount = int(input())
yuan_amount = float(input())
change_fee = float(input())

bitcoin_price_bgn = bitcoin_amount * 1168
yuan_price_usd = 0.15
usd_price_bgn = 1.76
yuan_price_bgn = (yuan_price_usd * yuan_amount) * 1.76
euro_price_bgn = 1.95

total_bgn = bitcoin_price_bgn + yuan_price_bgn
total_eur = 1 / 1.95 * total_bgn
total_fee = total_eur * (change_fee / 100)
total_eur -= total_fee

print(f"{total_eur:.2f}")
