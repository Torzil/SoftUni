length = int(input())
width = int(input())
height = int(input())
percentage_not_empty = float(input())

total_volume_centimeters = length * width * height
total_volume_liters = total_volume_centimeters / (10**3)
needed_water_liters = total_volume_liters - total_volume_liters \
                      * (percentage_not_empty / 100)

print (needed_water_liters)