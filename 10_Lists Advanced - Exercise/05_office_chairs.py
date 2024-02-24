number_of_rooms = int(input())
total_free_chairs = 0
for current_room in range(1, number_of_rooms+1):
    current_chairs = input().split()
    chairs = len(current_chairs[0])
    people = int(current_chairs[1])
    difference = chairs - people
    total_free_chairs += difference
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {current_room}")

if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")

