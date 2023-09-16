for _ in range(int(input())):
    mat = [[input() for x in range(9)] for y in range(9)]
    for i in range(2, 8):
        for j in range(2, 8):
            if mat[i][j] == '#' and mat[i-1][j-1] == '#' and mat[i-1][j+1] == '#'\
                    and mat[i+1][j-1] == '#' and mat[i+1][j+1] == '#':
                print(i, j, '\n')
