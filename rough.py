for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    f = 0
    ans = []
    for i in range(n-1):
        if l[i]>l[i+1]:
            f = 1
            if f==1:
                ans.append(l[i])
                ans.append(l[i+1] - 1)
        else:
            ans.append(l[i])
    print(ans)
