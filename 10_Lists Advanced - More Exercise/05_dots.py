def largest_connected_dots(grid):
    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '.':
            return 0
        count = 1
        grid[i][j] = 'X'
        count += dfs(i + 1, j)
        count += dfs(i - 1, j)
        count += dfs(i, j + 1)
        count += dfs(i, j - 1)
        return count

    max_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                max_count = max(max_count, dfs(i, j))
    return max_count


num_rows = int(input())


board = []
for _ in range(num_rows):
    row = input().split()
    board.append(row)


largest_count = largest_connected_dots(board)
print(largest_count)
