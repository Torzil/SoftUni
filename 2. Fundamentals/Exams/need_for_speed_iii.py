number_of_cars = int(input())
garage = {}

for _ in range(number_of_cars):
    current_car = input().split('|')
    model = current_car[0]
    start_mileage = int(current_car[1])
    start_fuel = int(current_car[2])
    if model not in garage:
        garage[model] = {"Mileage": 0, "Fuel": 0}
    garage[model]["Mileage"] = start_mileage
    garage[model]["Fuel"] = start_fuel


def drive(driven_car, drive_distance, needed_fuel):
    if garage[driven_car]["Fuel"] >= needed_fuel:
        garage[driven_car]["Fuel"] -= needed_fuel
        garage[driven_car]["Mileage"] += drive_distance
        if garage[driven_car]["Mileage"] < 100000:
            return f"{driven_car} driven for {drive_distance} kilometers. {needed_fuel} liters of fuel consumed."
        else:
            del garage[driven_car]
            return (f"{driven_car} driven for {drive_distance} kilometers. {needed_fuel} liters of fuel consumed.\n"
                    f"Time to sell the {driven_car}!")
    else:
        return "Not enough fuel to make that ride"


def refuel(refueled_car, fuel_liters):
    if garage[refueled_car]["Fuel"] + fuel_liters <= 75:
        garage[refueled_car]["Fuel"] += fuel_liters
        return f"{refueled_car} refueled with {fuel_liters} liters"
    else:
        fuel_liters = 75 - garage[refueled_car]["Fuel"]
        garage[refueled_car]["Fuel"] += fuel_liters
        return f"{refueled_car} refueled with {fuel_liters} liters"


def revert(reverted_car, reverted_miles):
    if garage[reverted_car]["Mileage"] - reverted_miles >= 10000:
        garage[reverted_car]["Mileage"] -= reverted_miles
        print(f"{reverted_car} mileage decreased by {reverted_miles} kilometers")
    else:
        garage[reverted_car]["Mileage"] = 10000


while True:
    command = input()

    if command == "Stop":
        break

    command = command.split(" : ")
    action = command[0]

    if action == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        print(drive(car, distance, fuel))

    elif action == "Refuel":
        car = command[1]
        fuel = int(command[2])
        print(refuel(car, fuel))

    elif action == "Revert":
        car = command[1]
        distance = int(command[2])
        revert(car, distance)

for key in garage.keys():
    print(f"{key} -> Mileage: {garage[key]['Mileage']} kms, Fuel in the tank: {garage[key]['Fuel']} lt.")
