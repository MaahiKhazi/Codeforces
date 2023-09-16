from collections import defaultdict

for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        v = list(map(int, input().split()))
        l.append(v)
    sl = sorted(l, key=lambda x: (x[0], -x[1]))
    c = 0
    ans = 0
    print(sl)
    for i in range(len(sl)):
        ans += sl[i][1]
        c += 1
        for j in range(len(sl)):
            if c >= sl[j][0]:
                sl.pop(j)
                c -= 1
                break
    print(ans)
