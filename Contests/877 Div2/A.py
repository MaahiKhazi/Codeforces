for _ in range(int(input())):
    n = input()
    l = list(map(int, input().split()))
    ans = 0
    for i in l:
        if i < 0:
            ans = i
            break
        else:
            ans = max(l)
    print(ans)

