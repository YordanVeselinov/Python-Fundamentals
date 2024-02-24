the_force = {}
while True:
    line = input()
    if line == "Lumpawaroo":
        break
    if "|" in line:
        force_side, force_user = line.split(" | ")
        if force_side not in the_force.keys():
            the_force[force_side] = []
        user_not_found = True
        for value in the_force.values():
            if force_user in value:
                user_not_found = False
        if user_not_found:
            the_force[force_side].append(force_user)

    elif "->" in line:
        force_user, force_side = line.split(" -> ")
        for value in the_force.values():
            if force_user in value:
                value.remove(force_user)
                break
        if force_side not in the_force.keys():
            the_force[force_side] = []
        the_force[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for key, value in the_force.items():
    if len(value) > 0:
        print(f"Side: {key}, Members: {len(value)}")
        for current in value:
            print(f"! {current}")
