to_do_list = []
while True:
    note = input()

    if note == "End":
        break
    to_do_list.append(note)

sorted_notes = sorted(to_do_list, key=lambda x: int(x.split("-")[0]))
result = [s.split("-")[1] for s in sorted_notes]
print(result)