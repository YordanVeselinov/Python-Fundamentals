first_line = [int(number) for number in input().split()]
second_line = [int(number) for number in input().split()]
third_line = [int(number) for number in input().split()]
is_first_winner = False
is_second_winner = False
is_draw = False
# Checking for the first winner
if first_line[0] == 1 and first_line[1] == 1 and first_line[2] == 1:
    is_first_winner = True
elif second_line[0] == 1 and second_line[1] == 1 and second_line[2] == 1:
    is_first_winner = True
elif third_line[0] == 1 and third_line[1] == 1 and third_line[2] == 1:
    is_first_winner = True
elif first_line [0] == 1 and second_line[0] == 1 and third_line[0] == 1:
    is_first_winner = True
elif first_line [1] == 1 and second_line[1] == 1 and third_line[1] == 1:
    is_first_winner = True
elif first_line [2] == 1 and second_line[2] == 1 and third_line[2] == 1:
    is_first_winner = True
elif first_line[0] == 1 and second_line[1] == 1 and third_line[2] == 1:
    is_first_winner = True
elif first_line[2] == 1 and second_line[1] == 1 and third_line[0] == 1:
    is_first_winner = True

# Starting to check for the second winner
elif first_line[0] == 2 and first_line[1] == 2 and first_line[2] == 2:
    is_second_winner = True
elif second_line[0] == 2 and second_line[1] == 2 and second_line[2] == 2:
    is_second_winner = True
elif third_line[0] == 2 and third_line[1] == 2 and third_line[2] == 2:
    is_second_winner = True
elif first_line [0] == 2 and second_line[0] == 2 and third_line[0] == 2:
    is_second_winner = True
elif first_line [1] == 2 and second_line[1] == 2 and third_line[1] == 2:
    is_second_winner = True
elif first_line [2] == 2 and second_line[2] == 2 and third_line[2] == 2:
    is_second_winner= True
elif first_line[0] == 2 and second_line[1] == 2 and third_line[2] == 2:
    is_second_winner = True
elif first_line[2] == 2 and second_line[1] == 2 and third_line[0] == 2:
    is_second_winner = True
else:
    is_draw = True

if is_first_winner:
    print("First player won")
elif is_second_winner:
    print("Second player won")
elif is_draw:
    print("Draw!")