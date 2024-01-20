number_of_students = int(input())
average_grade = 0
grades_between_2_3 = 0
grades_between_3_4 = 0
grades_between_4_5 = 0
grades_over_5 = 0

for student in range(number_of_students):
    current_grade = float(input())
    if current_grade < 3:
        average_grade += current_grade
        grades_between_2_3 += 1
    elif current_grade < 4:
        average_grade += current_grade
        grades_between_3_4 += 1
    elif current_grade < 5:
        average_grade += current_grade
        grades_between_4_5 += 1
    elif current_grade >= 5:
        average_grade += current_grade
        grades_over_5 += 1

average_grade /= number_of_students
percentage_grades_between_2_3 = grades_between_2_3 / number_of_students * 100
percentage_grades_between_3_4 = grades_between_3_4 / number_of_students * 100
percentage_grades_between_4_5 = grades_between_4_5 / number_of_students * 100
percentage_grades_over_5 = grades_over_5 / number_of_students * 100

print(f"Top students: {percentage_grades_over_5:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_grades_between_4_5:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_grades_between_3_4:.2f}%")
print(f"Fail: {percentage_grades_between_2_3:.2f}%")
print(f"Average: {average_grade:.2f}")
