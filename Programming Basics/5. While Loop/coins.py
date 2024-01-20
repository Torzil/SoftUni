user_money = float(input())
inserted_coins = int(user_money * 100)
change_coins_counter = 0

while inserted_coins > 0:
    if inserted_coins // 200:
        inserted_coins -= 200
        change_coins_counter += 1
    elif inserted_coins // 100:
        inserted_coins -= 100
        change_coins_counter += 1
    elif inserted_coins // 50:
        inserted_coins -= 50
        change_coins_counter += 1
    elif inserted_coins // 20:
        inserted_coins -= 20
        change_coins_counter += 1
    elif inserted_coins // 10:
        inserted_coins -= 10
        change_coins_counter += 1
    elif inserted_coins // 5:
        inserted_coins -= 5
        change_coins_counter += 1
    elif inserted_coins // 2:
        inserted_coins -= 2
        change_coins_counter += 1
    elif inserted_coins // 1:
        inserted_coins -= 1
        change_coins_counter += 1

print(change_coins_counter)
