for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))
    # d = [0] * n
    t = 0
    for i in range(n):
        t = max(t, s[i])
        print(f[i] - t, end=' ')
        t = f[i]
    print('')
    # for ans in d:
    #   print(ans)

