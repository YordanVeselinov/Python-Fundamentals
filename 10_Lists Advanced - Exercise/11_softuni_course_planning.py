lectures = [lecture for lecture in input().split(", ")]

while True:
    new_lecture = input().split(":")
    if new_lecture[0] == "course start":
        break
    elif new_lecture[0] == "Add":
        if new_lecture[1] not in lectures:
            lectures.append(new_lecture[1])
    elif new_lecture[0] == "Insert":
        if new_lecture[1] not in lectures:
            index = new_lecture[2]
            lectures.insert(int(index), new_lecture[1])

    elif new_lecture[0] == "Remove":
        if new_lecture[1] in lectures:
            index = lectures.index(new_lecture[1])
            if lectures[index+1] == f"{new_lecture[1]}-Exercise":
                lectures.remove(f"{new_lecture[1]}-Exercise")
            lectures.remove(new_lecture[1])
    elif new_lecture[0] == "Swap":
        if new_lecture[1] in lectures and new_lecture[2] in lectures:
            first_index = lectures.index(new_lecture[1])
            second_index = lectures.index(new_lecture[2])
            lectures[first_index], lectures[second_index] = lectures[second_index], lectures[first_index]
            if len(lectures) > second_index+1:
                if lectures[first_index+1] == f"{new_lecture[1]}-Exercise":
                    lectures.insert(second_index+1,f"{new_lecture[1]}-Exercise")
                    lectures.pop(first_index+2)
                elif lectures[second_index+1] == f"{new_lecture[2]}-Exercise":
                    lectures.insert(first_index+1,f"{new_lecture[2]}-Exercise")
                    lectures.pop(second_index+2)
                elif lectures[second_index+1] == f"{new_lecture[2]}-Exercise" and lectures[first_index+1] == f"{new_lecture[1]}-Exercise":
                    lectures.insert(first_index+1,f"{new_lecture[2]}-Exercise")
                    lectures.pop(second_index+2)
                    lectures.insert(second_index+1,f"{new_lecture[1]}-Exercise")
                    lectures.pop(first_index+2)
    elif new_lecture[0] == "Exercise":
        if new_lecture[1] in lectures and f"{new_lecture[1]}-Exercise" not in lectures:
            index_lecture = lectures.index(new_lecture[1])
            lectures.insert(index_lecture+1,f"{new_lecture[1]}-Exercise")
        else:
            lectures.append(new_lecture[1])
            lectures.append(f"{new_lecture[1]}-{new_lecture[0]}")

index = 0
for current_lecture in range(1, len(lectures)+1):
    print(f"{current_lecture}.{lectures[index]}")
    index += 1


