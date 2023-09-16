for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
    else:
        if n % 2 != 0:
            print(-1)
        else:
            l = [i+1 for i in range(n)]
            for i in range(0, n - 1, 2):
                l[i], l[i + 1] = l[i + 1], l[i]
            print(*l)
