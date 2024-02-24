days = int(input())
plunder_per_day = int(input())
expected_plunder = int(input())
gathered_plunder = 0

for current_day in range(1 , days + 1):
    gathered_plunder += plunder_per_day
    if current_day % 3 == 0:
        gathered_plunder += 0.50 * plunder_per_day
    if current_day % 5 == 0:
        gathered_plunder -= gathered_plunder * 0.30

if gathered_plunder >= expected_plunder:
    print(f"Ahoy! {gathered_plunder:.2f} plunder gained.")
else:
    percentage = (gathered_plunder / expected_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")