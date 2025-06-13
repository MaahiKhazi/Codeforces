for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    sl = sorted(l, reverse=True)
    ind = []
    for i in sl:
        ind.append(l.index(i))
    print(ind)
    a = ind[:k]
    print(a)