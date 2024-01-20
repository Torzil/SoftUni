stadium_capacity = int(input())
total_fans = int(input())
sector_A_fans = 0
sector_B_fans = 0
sector_V_fans = 0
sector_G_fans = 0

for fan in range(total_fans):
    sector = input()
    if sector == "A":
        sector_A_fans += 1
    elif sector == "B":
        sector_B_fans += 1
    elif sector == "V":
        sector_V_fans += 1
    elif sector == "G":
        sector_G_fans += 1

percent_stadium_full = total_fans / stadium_capacity * 100
percent_sector_A_fans = sector_A_fans / total_fans * 100
percent_sector_B_fans = sector_B_fans / total_fans * 100
percent_sector_V_fans = sector_V_fans / total_fans * 100
percent_sector_G_fans = sector_G_fans / total_fans * 100

print(f"{percent_sector_A_fans:.2f}%")
print(f"{percent_sector_B_fans:.2f}%")
print(f"{percent_sector_V_fans:.2f}%")
print(f"{percent_sector_G_fans:.2f}%")
print(f"{percent_stadium_full:.2f}%")
