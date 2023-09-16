for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = set(a)
    res = len(ans)
    print(res)