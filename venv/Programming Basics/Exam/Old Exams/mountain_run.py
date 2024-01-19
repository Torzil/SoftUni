record_time = float(input())
distance_to_run = float(input())
time_per_1_meter = float(input())

slope_slowing = (distance_to_run // 50) * 30
run_time = distance_to_run * time_per_1_meter + slope_slowing

if run_time < record_time:
    print(f"Yes! The new record is {run_time:.2f} seconds.")
else:
    difference = run_time - record_time
    print(f"No! He was {difference:.2f} seconds slower.")
