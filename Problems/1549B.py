for _ in range(int(input())):
    n = int(input())
    e = list(input())
    g = list(input())
    ans = 0
    for i in range(n):
        p = g[i]
        if p == '0':
            continue
        if e[i] == "0":
            ans += 1
        elif i - 1 >= 0 and e[i - 1] == '1':
            ans += 1
        elif i + 1 < n and e[i + 1] == '1':
            e[i + 1] = '2'
            ans += 1
    print(ans)
