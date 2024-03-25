courses = {}

while True:
    command = input().split(" : ")

    if command[0] == "end":
        break

    course = command[0]
    student = command[1]

    if course not in courses:
        courses[course] = []
    courses[course].append(student)

for current_course, students in courses.items():
    print(f"{current_course}: {len(students)}")
    for current_student in students:
        print(f"-- {current_student}")
