number_of_pages = int(input())
pages_per_hour = int(input())
days_needed = int(input())

time_per_day = (number_of_pages / pages_per_hour) / days_needed

print(int(time_per_day))
