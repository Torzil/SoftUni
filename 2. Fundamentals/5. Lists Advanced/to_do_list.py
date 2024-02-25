def to_do_list():
    tasks = []
    while True:
        current_task = input()

        if current_task == "End":
            break

        tasks.append(current_task)

    sorted_tasks = sorted(tasks, key=lambda x: int(x.split("-")[0]))
    sorted_tasks = [task.split("-")[1] for task in sorted_tasks]

    return sorted_tasks


result = to_do_list()
print(result)
