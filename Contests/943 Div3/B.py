for _ in range(int(input())):
    n, m = map(int, input().split())
    a = input()
    b = input()
    i = 0
    j = 0
    ans = 0
    while i < n and j < m:
        if a[i] == b[j]:
            i += 1
            ans += 1
        j += 1
    print(ans)