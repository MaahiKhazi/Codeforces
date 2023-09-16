for _ in range(int(input())):
    n = int(input())
    ans = []
    ans.append(1)
    d = {}
    d[1] = 1
    for i in range(2, n+1):
        if d.get(i, 0) == 1:
            continue
        x = i
        while x<=n:
            if d.get(x, 0) != 1:
                ans.append(x)
                d[x] = 1
                x*=2
    print(*ans)
