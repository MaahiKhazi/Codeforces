def equals(a, b, n):
    inf = 1e9 + 7
    min_diff = inf
    for i in range(n):
        if b[i] != 0:
            min_diff = min(min_diff, a[i] - b[i])
    if min_diff < 0:
        return False
    if min_diff == inf:
        return True
    for i in range(n):
        if a[i] - b[i] > min_diff:
            return False
        if b[i] != 0 and a[i] - b[i] < min_diff:
            return False
    return True


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if equals(a, b, n) == 1:
        print('YES')
    else:
        print('NO')

