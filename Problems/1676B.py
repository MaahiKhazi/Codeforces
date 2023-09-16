for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    loc = min(c)
    for i in range(n):
        c[i] = c[i] - loc
    ans = sum(c)
    print(ans)