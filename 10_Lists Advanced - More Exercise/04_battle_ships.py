
num_rows = int(input())


field = []
for _ in range(num_rows):
    row = list(map(int, input().split()))
    field.append(row)


def count_ships_destroyed(board, attacks):
    destroyed_ships = 0
    for attack in attacks:
        row, col = map(int, attack.split('-'))
        if board[row][col] > 0:
            board[row][col] -= 1
            if board[row][col] == 0:
                destroyed_ships += 1
    return destroyed_ships


attack_list = input().split()


ships_destroyed = count_ships_destroyed(field, attack_list)
print(ships_destroyed)
