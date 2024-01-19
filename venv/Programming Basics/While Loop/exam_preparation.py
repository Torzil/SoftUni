max_bad_grades = int(input())
average_grade = 0
problem_counter = 0
bad_grades_counter = 0
last_problem = ""
too_many_bad_grades = False


current_problem = input()
while current_problem != "Enough":
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == max_bad_grades:
            too_many_bad_grades = True
            break
    average_grade += current_grade
    problem_counter += 1
    last_problem = current_problem
    current_problem = input()
if too_many_bad_grades:
    print(f"You need a break, {bad_grades_counter} poor grades.")
else:
    average_grade /= problem_counter
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {problem_counter}")
    print(f"Last problem: {last_problem}")
