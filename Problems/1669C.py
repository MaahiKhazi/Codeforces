for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    e1, e2, o1, o2 = 0, 0, 0, 0
    for i in range(n):
        if i % 2 == 1:
            if a[i] % 2 == 1:
                o1 = 1
            else:
                e1 = 1
        else:
            if a[i] % 2 == 1:
                o2 = 1
            else:
                e2 = 1
    if e1 and o1:
        print('NO')
    elif e2 and o2:
        print('NO')
    else:
        print('YES')

