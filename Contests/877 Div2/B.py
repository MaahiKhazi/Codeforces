for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    m = 0
    o = 0
    t = 0
    for i in range(n):
        if l[i] == 1:
            o = i + 1
        if l[i] == 2:
            t = i + 1
        if l[m] < l[i]:
            m = i
    m += 1
    if o < m and t < m:
        if o > t:
            print(o, m)
        else:
            print(t, m)
    elif o > m and t > m:
        if o > t:
            print(t, m)
        else:
            print(o, m)
    else:
        print(n, n)
