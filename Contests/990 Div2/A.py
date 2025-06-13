for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    k = 1
    total = 1
    h = 0
    mp = sum(l)
    sl = []
    while total<=mp:
        sl.append(total)
        k += 1
        total += 8*(k-1)
    rt = 0
    for i in range(n):
        rt += l[i]
        if rt in sl:
            h += 1
    print(h)
