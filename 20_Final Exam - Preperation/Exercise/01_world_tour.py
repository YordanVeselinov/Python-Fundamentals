stops = input()
while True:
    command = input().split(":")
    if command[0] == "Travel":
        break
    action = command[0]
    if action == "Add Stop":
        index, string = int(command[1]), command[2]
        if index < len(stops):
            stops = stops[:index] + string + stops[index:]
    elif action == "Remove Stop":
        start_index , stop_index = int(command[1]), int(command[2])
        if start_index >= 0 and stop_index < len(stops):
            stops = stops[:start_index] + stops[stop_index+1:]
    elif action == "Switch":
        old_string, new_string = command[1], command[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    print(stops)
print(f"Ready for world tour! Planned stops: {stops}")