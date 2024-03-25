companies = {}

while True:
    command = input().split(" -> ")

    if command[0] == "End":
        break

    company_name = command[0]
    employee_id = command[1]

    if company_name not in companies:
        companies[company_name] = []
    if employee_id not in companies[company_name]:
        companies[company_name].append(employee_id)

for company, employees in companies.items():
    print(company)
    for e_id in employees:
        print(f"-- {e_id}")
