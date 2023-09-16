for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    b = []
    c = []
    if len(set(l)) == 1:
        print(-1)
    else:
        l.sort()
        le = l[-1]
        for i in l:
            if i == le:
                c.append(i)
            else:
                b.append(i)
        print(len(b), len(c))        
        print(*b)
        print(*c)