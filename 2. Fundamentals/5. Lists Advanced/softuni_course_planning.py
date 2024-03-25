def add_lesson(title):
    if title not in schedule:
        schedule.append(title)


def insert_lesson(title, index):
    if title not in schedule:
        schedule.insert(int(index), title)


def remove_lesson(title):
    if title + "-Exercise" in schedule:
        schedule.remove(title + "-Exercise")
    if title in schedule:
        schedule.remove(title)


def swap_lessons(title1, title2):
    if title1 in schedule and title2 in schedule:
        index_1 = schedule.index(title1)
        index_2 = schedule.index(title2)
        schedule[index_1], schedule[index_2] = schedule[index_2], schedule[index_1]
    if title1 + "-Exercise" in schedule:
        schedule.remove(title1 + "-Exercise")
        schedule.insert(index_2 + 1, title1 + "-Exercise")
    if title2 + "-Exercise" in schedule:
        schedule.remove(title2 + "-Exercise")
        schedule.insert(index_1 + 1, title2 + "-Exercise")


def add_exercise(title):
    if title in schedule:
        if title + "-Exercise" not in schedule:
            exercise_index = schedule.index(title) + 1
            schedule.insert(exercise_index, title + "-Exercise")
    elif title not in schedule:
        if title + "-Exercise" in schedule:
            exercise_index = schedule.index(title + "-Exercise")
            schedule.insert(exercise_index, title)
        else:
            added_lesson = [title, title + "-Exercise"]
            schedule.extend(added_lesson)


schedule = input().split(", ")
action = input()
while action != "course start":
    action = action.split(":")
    if action[0] == "Add":
        add_lesson(action[1])
    elif action[0] == "Insert":
        insert_lesson(action[1], action[2])
    elif action[0] == "Remove":
        remove_lesson(action[1])
    elif action[0] == "Swap":
        swap_lessons(action[1], action[2])
    elif action[0] == "Exercise":
        add_exercise(action[1])
    action = input()

for lesson in schedule:
    current_index = schedule.index(lesson) + 1
    print(f"{current_index}.{lesson}")
