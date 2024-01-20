period_of_time = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0
days_passed = 0

for day in range(period_of_time):
    days_passed += 1
    if days_passed % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    number_of_patients = int(input())
    if number_of_patients <= doctors:
        treated_patients += number_of_patients
    else:
        treated_patients += doctors
    if number_of_patients > doctors:
        untreated_patients += number_of_patients - doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
