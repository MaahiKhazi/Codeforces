for _ in range(int(input())):
    m, k, a, ak = map(int, input().split())
    kb = ak * k
    res = 0
    if m < a or m < kb:
        print(0)
    else:
        lb = m - kb
        if (lb-a)%k == 0:
            ans = (lb-a)//k
            print(ans)
        else:
            ans = (lb-(a-(m%k)))//k
            print(ans)