for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = [0]*(n+1)
    ans[0] = l[0] + 1
    for i in range(1, n):
        ans[i] = l[i-1]+ans[i-1]
    ans.remove(ans[len(ans)-1])
    print(*ans)