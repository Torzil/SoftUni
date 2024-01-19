budget = float(input())
number_of_video_cards = int(input())
number_of_processors = int(input())
number_of_ram_sticks = int(input())

video_card_price = 250
processor_price = (video_card_price * number_of_video_cards) * 0.35
ram_stick_price = (video_card_price * number_of_video_cards) * 0.10

total_price = number_of_video_cards * video_card_price \
    + number_of_processors * processor_price \
    + number_of_ram_sticks * ram_stick_price

if number_of_video_cards > number_of_processors:
    total_price -= total_price * 0.15

difference = abs(budget - total_price)

if budget >= total_price:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
