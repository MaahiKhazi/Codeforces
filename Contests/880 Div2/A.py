for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    if l.count(0) == 0:
        print('NO')
    elif l.count(0) >= l.count(1) >= l.count(2):
        print('YES')
    else:
        print('NO')
