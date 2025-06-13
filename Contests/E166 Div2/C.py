for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    p = []
    t = []
    loa = []
    ans = []
    for i in range(n+m+1):
        loa.append([a[:i] + a[i+1:], b[:i] + b[i+1:]])
    # print(loa[0][0], loa[0][1])
    for i in range(n+m+1):
        if n>0 and m>0:
            for j in range(n+m):
                if loa[i][0][j] > loa[i][1][j]:
                    p.append(loa[i][0][j])
                else:
                    t.append(loa[i][1][j])
        elif n>0 and m==0:
            for j in range(n+m):
                p.append(loa[i][0][j])
            if ans:
                ans.append(sum(p)-sum(ans))
            else:
                ans.append(sum(p))
        elif n==0 and m>0:
            for j in range(n+m):
                t.append(loa[i][1][j])
            if ans:
                ans.append(sum(t)-sum(ans))
            else:
                ans.append(sum(t))
        elif n==0 and m==0:
            print(0)
    print(p, t, ans)