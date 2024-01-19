destination = input()
package_type = input()
vip_discount = input()
days_stayed = int(input())
price_per_day = 0
number_is_invalid = False
invalid_input = False

if days_stayed < 1:
    number_is_invalid = True

if days_stayed > 7:
    days_stayed -= 1
    
if destination == "Bansko" or destination == "Borovets":
    if package_type == "withEquipment":
        price_per_day = 100
        if vip_discount == "yes":
            price_per_day *= 0.9
    elif package_type == "noEquipment":
        price_per_day = 80
        if vip_discount == "yes":
            price_per_day *= 0.95
    else:
        invalid_input = True
elif destination == "Varna" or destination == "Burgas":
    if package_type == "withBreakfast":
        price_per_day = 130
        if vip_discount == "yes":
            price_per_day *= 0.88
    elif package_type == "noBreakfast":
        price_per_day = 100
        if vip_discount == "yes":
            price_per_day *= 0.93
    else:
        invalid_input = True
else:
    invalid_input = True

total_price = days_stayed * price_per_day

if number_is_invalid:
    print("Days must be positive number!")
elif invalid_input:
    print("Invalid input!")
else:
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
