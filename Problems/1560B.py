for _ in range(int(input())):
    a, b, c = map(int, input().split())
    ans = 2*abs(a-b)
    if a > ans or b > ans or c > ans:
        print(-1)
    else:
        res = (ans//2) + c
        while res > ans:
            res -= ans
        print(res)
