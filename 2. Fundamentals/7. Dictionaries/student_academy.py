students_count = int(input())
academy = {}

for _ in range(students_count):
    student = input()
    grade = float(input())

    if student not in academy:
        academy[student] = []
    academy[student].append(grade)

for current_student, current_grades in academy.items():
    average_grade = sum(current_grades) / len(current_grades)
    if average_grade >= 4.50:
        print(f"{current_student} -> {average_grade:.2f}")
