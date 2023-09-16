for _ in range(int(input())):
    n = int(input())
    sme = []
    mi = []
    if n==1:
        m = int(input())
        l = list(map(int, input().split()))
        print(min(l))
    else:
        for i in range(n):
            m = int(input())
            l = list(map(int, input().split()))
            l.sort()
            mi.append(l[0])
            sme.append(l[1])
        mi.sort()
        sme.sort()
        print(mi[0] + sum(sme[1:]))

