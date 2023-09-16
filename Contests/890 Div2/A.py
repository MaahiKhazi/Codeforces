for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if l[i] > l[i+1]:
            ans = max(ans, l[i])
    print(ans)
    