for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = a[n-1] - a[0]
    for i in range(n-1):
        ans = min(ans, a[i+1] - a[i])
    print(ans)