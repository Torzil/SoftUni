chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15

total_price = chicken_menus * chicken_menu_price \
    + fish_menus * fish_menu_price \
    + vegetarian_menus * vegetarian_menu_price

dessert_price = total_price * 0.2
delivery_price = 2.50

final_price = total_price + dessert_price + delivery_price

print (final_price)