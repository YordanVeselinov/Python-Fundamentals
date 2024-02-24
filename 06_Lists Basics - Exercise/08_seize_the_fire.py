fires_cells = input().split('#')
remaining_water = int(input())
effort = 0
total_fire = 0
put_out_cells = []

for current_fire_cell in fires_cells:
    current_list_cells = []
    current_list_cells = (current_fire_cell.split(" ="))
    if int(current_list_cells[1]) <= remaining_water:
        if current_list_cells[0] == "High":
            if 81 <= int(current_list_cells[1]) <= 125:
                total_fire += int(current_list_cells[1])
                remaining_water -= int(current_list_cells[1])
                effort += int(current_list_cells[1])
                put_out_cells.append(current_list_cells[1])
        elif current_list_cells[0] == "Medium":
            if 51 <= int(current_list_cells[1]) <= 80:
                total_fire += int(current_list_cells[1])
                remaining_water -= int(current_list_cells[1])
                effort += int(current_list_cells[1])
                put_out_cells.append(current_list_cells[1])
        elif current_list_cells[0] == "Low":
            if 1 <= int(current_list_cells[1]) <= 50:
                total_fire += int(current_list_cells[1])
                remaining_water -= int(current_list_cells[1])
                effort += int(current_list_cells[1])
                put_out_cells.append(current_list_cells[1])
    else:
        continue

print("Cells:")
for item in put_out_cells:
    print(f" -{item}")
print(f"Effort: {effort * 0.25:.2f}")
print(f"Total Fire: {total_fire}")


