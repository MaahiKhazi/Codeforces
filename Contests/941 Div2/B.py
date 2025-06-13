for _ in range(int(input())):
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        row = input()
        grid.append(row)
    x1, y1 = 0, 0
    if (grid[x1], grid[y1]) == (grid[len(grid) - 1], grid[len(grid[0]) - 1]):
        print("YES")
    else:
        print("NO")