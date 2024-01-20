exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 + arrival_minutes
hour = abs(exam_time - arrival_time) // 60
minutes = abs(exam_time - arrival_time) % 60

if arrival_time < exam_time - 30:
    print("Early")
    if arrival_time > exam_time - 60:
        print(f"{minutes} minutes before the start")
    elif arrival_time <= exam_time - 60:
        print(f"{hour}:{minutes:02d} hours before the start")
elif arrival_time <= exam_time:
    print("On time")
    if arrival_time > exam_time - 60:
        print(f"{minutes} minutes before the start")
elif arrival_time > exam_time:
    print("Late")
    if arrival_time < exam_time + 60:
        print(f"{minutes} minutes after the start")
    elif arrival_time >= exam_time + 60:
        print(f"{hour}:{minutes:02d} hours after the start")
