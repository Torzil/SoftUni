number_of_groups = int(input())
musala_climbers = 0
montblanc_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0
total_climbers = 0

for group in range(number_of_groups):
    climbers_in_group = int(input())
    if climbers_in_group < 6:
        musala_climbers += climbers_in_group
    elif climbers_in_group < 13:
        montblanc_climbers += climbers_in_group
    elif climbers_in_group < 26:
        kilimanjaro_climbers += climbers_in_group
    elif climbers_in_group < 41:
        k2_climbers += climbers_in_group
    elif climbers_in_group >= 41:
        everest_climbers += climbers_in_group
    total_climbers += climbers_in_group

percent_musala_climbers = musala_climbers / total_climbers * 100
percent_montblanc_climbers = montblanc_climbers / total_climbers * 100
percent_kilimanjaro_climbers = kilimanjaro_climbers / total_climbers * 100
percent_k2_climbers = k2_climbers / total_climbers * 100
percent_everest_climbers = everest_climbers / total_climbers * 100

print(f"{percent_musala_climbers:.2f}%")
print(f"{percent_montblanc_climbers:.2f}%")
print(f"{percent_kilimanjaro_climbers:.2f}%")
print(f"{percent_k2_climbers:.2f}%")
print(f"{percent_everest_climbers:.2f}%")
