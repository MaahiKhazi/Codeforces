for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a<b<c or (a<b and b>c):
        print('YES')
    else:
        print('NO')