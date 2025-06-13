for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    cnt = 0
    lb = b[-1]
    ce = min(a, key=lambda x: (abs(x - lb), x))
    ce_b = min((x for x in b[:-1]), key=lambda x: (abs(x - lb), x))
    if abs(ce - lb) <= abs(ce_b - lb):
        v = ce
    else:
        v = ce_b
    for i in range(n):
        if min(a[i], b[i]) < lb < max(a[i], b[i]):
            cnt = 1
        ans += abs(a[i]-b[i])
    if cnt:
        ans += 1
    else:
        ans += abs(b[-1] - v) + 1
    print(ans)