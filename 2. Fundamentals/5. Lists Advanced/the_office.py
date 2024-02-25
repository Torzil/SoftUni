employee_list = list(map(int, input().split()))
improvement_factor = int(input())


def happiness_detector():
    happiness_list = [h * improvement_factor for h in employee_list]
    average_happiness = sum(happiness_list) / len(happiness_list)
    happy_employees = [e for e in happiness_list if e >= average_happiness]
    score = f"{len(happy_employees)}/{len(employee_list)}"
    are_employees_happy = "happy" if len(happy_employees) >= (len(employee_list) / 2) else "not happy"
    print(f"Score: {score}. Employees are {are_employees_happy}!")


happiness_detector()
