student_name = input()

grade_sum = 0
average_grade = 0
fail_count = 0
year = 0

while True:
    current_grade = float(input())

    if current_grade < 4:
        fail_count += 1
        if fail_count > 1:
            print(f"{student_name} has been excluded at {year + 1} grade")
            break
        else:
            continue

    grade_sum += current_grade
    year += 1
    if year == 12:
        average_grade = grade_sum / 12
        print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
        break
