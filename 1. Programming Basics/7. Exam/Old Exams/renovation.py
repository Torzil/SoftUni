from math import ceil

wall_height = int(input())
wall_width = int(input())
percentage_to_not_paint = int(input())
total_area_to_paint = wall_width * wall_height * 4
total_area_to_paint -= ceil(total_area_to_paint * (percentage_to_not_paint / 100))
job_is_done = False

liters_of_paint = input()
while liters_of_paint != "Tired!":
    liters_of_paint = int(liters_of_paint)
    total_area_to_paint -= liters_of_paint
    if total_area_to_paint <= 0:
        job_is_done = True
        break
    liters_of_paint = input()

if job_is_done:
    if total_area_to_paint < 0:
        print(f"All walls are painted and you have {abs(total_area_to_paint)} l paint left!")
    else:
        print("All walls are painted! Great job, Pesho!")
else:
    print(f"{total_area_to_paint} quadratic m left.")
