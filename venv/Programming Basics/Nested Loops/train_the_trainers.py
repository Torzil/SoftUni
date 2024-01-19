number_of_judges = int(input())
number_of_grades = 0
total_grade_average = 0

current_presentation = input()
while current_presentation != "Finish":
    average_grade = 0
    for judge in range(number_of_judges):
        current_grade = float(input())
        average_grade += current_grade
    average_grade /= number_of_judges
    total_grade_average += average_grade
    number_of_grades += 1
    print(f"{current_presentation} - {average_grade:.2f}.")
    current_presentation = input()

total_grade_average /= number_of_grades

print(f"Student's final assessment is {total_grade_average:.2f}.")
