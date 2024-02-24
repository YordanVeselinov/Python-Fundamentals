maze_size = int(input())

maze = []
for _ in range(maze_size):
    row = list(input().strip())
    maze.append(row)

n = len(maze)
m = len(maze[0])


def is_valid(x, y):
    return 0 <= x < n and 0 <= y < m and maze[x][y] == ' '


kate_pos = None
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(n):
    if 'k' in maze[i]:
        kate_pos = (i, maze[i].index('k'))
        break

if kate_pos:
    max_moves = 0
    found_exit = False
    for direction in directions:
        x, y = kate_pos
        moves = 0
        while is_valid(x + direction[0], y + direction[1]):
            moves += 1
            maze[x][y] = '#'
            x += direction[0]
            y += direction[1]
        if moves > max_moves:
            max_moves = moves
            found_exit = True

    if found_exit:
        print(f"Kate got out in {max_moves} moves")
    else:
        print("Kate cannot get out")
else:
    print("Kate cannot get out")
