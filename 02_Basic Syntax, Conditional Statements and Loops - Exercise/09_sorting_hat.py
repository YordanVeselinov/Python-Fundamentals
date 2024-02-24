name_command = input()

while name_command != "Welcome":
    if name_command == "Voldemort":
        print("You must not speak of that name!")
        break
    elif name_command == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    elif len(name_command) < 5:
        print(f"{name_command} goes to Gryffindor.")
    elif len(name_command) == 5:
        print(f"{name_command} goes to Slytherin.")
    elif len(name_command) == 6:
        print(f"{name_command} goes to Ravenclaw.")
    elif len(name_command) > 6:
        print(f"{name_command} goes to Hufflepuff.")

    name_command = input()
