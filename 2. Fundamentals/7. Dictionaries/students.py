students = {}

while True:
    student = input().split(":")

    if len(student) == 1:
        course_as_list = student[0].split("_")
        course = " ".join(course_as_list)
        break
    student_name = student[0]
    student_id = student[1]
    student_course = student[2]

    if student_name not in students:
        students[student_name] = {student_id: student_course}

for s_name, s_info in students.items():
    for s_id, s_course in s_info.items():
        if course in s_course:
            print(f"{s_name} - {s_id}")
