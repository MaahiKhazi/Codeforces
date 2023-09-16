for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    a1 = l[0] * l[1]
    a2 = l[n - 2] * l[n-1]
    ans = max(a1, a2)
    print(ans)