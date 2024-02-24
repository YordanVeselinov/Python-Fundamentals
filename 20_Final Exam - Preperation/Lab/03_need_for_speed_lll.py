cars = {}
number_of_cars = int(input())
for n in range(number_of_cars):
    car, mileage, fuel = input().split("|")
    cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}
while True:
    command = input().split(" : ")
    if command[0] == "Stop":
        break
    if command[0] == "Drive":
        current_car, distance, fuel = command[1], int(command[2]), int(command[3])
        if cars[current_car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[current_car]["fuel"] -= fuel
            cars[current_car]["mileage"] += distance
            print(f"{current_car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[current_car]["mileage"] >= 100000:
                print(f"Time to sell the {current_car}!")
                cars.pop(current_car)
    elif command[0] == "Refuel":
        maximum_liter = 75
        current_car, fuel = command[1], int(command[2])
        fuel_to_add = min(fuel, maximum_liter - cars[current_car]["fuel"])
        cars[current_car]["fuel"] += fuel_to_add
        print(f"{current_car} refueled with {fuel_to_add} liters")
    elif command[0] == "Revert":

        current_car, kilometers = command[1], int(command[2])
        cars[current_car]["mileage"] -= kilometers
        if cars[current_car]["mileage"] < 10000:
            cars[current_car]["mileage"] = 10000
        else:
            print(f"{current_car} mileage decreased by {kilometers} kilometers")

for car, mileage_fuel in cars.items():
    print(f"{car} -> Mileage: {mileage_fuel['mileage']} kms, Fuel in the tank: {mileage_fuel['fuel']} lt.")