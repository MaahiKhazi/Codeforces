for _ in range(int(input())):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    max_val = l[0]
    for i in range(1, n):
        if l[i] < max_val:
            diff = max_val - l[i]
            if diff <= m:
                l[i] += diff
                m -= diff
            else:
                l[i] += m
                m = 0
    while m > 0:
        l[0] += 1
        m -= 1
        max_val = l[0]
        for i in range(1, len(l)):
            if l[i] < max_val:
                diff = max_val - l[i]
                if diff <= m:
                    l[i] += diff
                    m -= diff
                else:
                    l[i] += m
                    m = 0
    mini = min(l)
    ans = 0
    ans = mini + (mini-1)*(n-1)
    print(l)
    print(m, ans)