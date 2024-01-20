number_of_climber_groups = int(input())

musala_climbers = 0
montblanc_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0

for group in range(number_of_climber_groups):
    number_of_climbers = int(input())
    if number_of_climbers <= 5:
        musala_climbers += number_of_climbers
    elif number_of_climbers <= 12:
        montblanc_climbers += number_of_climbers
    elif number_of_climbers <= 25:
        kilimanjaro_climbers += number_of_climbers
    elif number_of_climbers <= 40:
        k2_climbers += number_of_climbers
    elif number_of_climbers >= 41:
        everest_climbers += number_of_climbers

total_number_of_climbers = musala_climbers\
                           + montblanc_climbers\
                           + kilimanjaro_climbers\
                           + k2_climbers\
                           + everest_climbers

percent_musala_climbers = musala_climbers / total_number_of_climbers * 100
percent_montblanc_climbers = montblanc_climbers / total_number_of_climbers * 100
percent_kilimanjaro_climbers = kilimanjaro_climbers / total_number_of_climbers * 100
percent_k2_climbers = k2_climbers / total_number_of_climbers * 100
percent_everest_climbers = everest_climbers / total_number_of_climbers * 100

print(f"{percent_musala_climbers:.2f}%")
print(f"{percent_montblanc_climbers:.2f}%")
print(f"{percent_kilimanjaro_climbers:.2f}%")
print(f"{percent_k2_climbers:.2f}%")
print(f"{percent_everest_climbers:.2f}%")
