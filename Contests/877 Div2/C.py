for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = []
    for r in range(0, n, 2):
        s = r*m+1
        row = list(range(s, s+m))
        ans.append(row)
    for r in range(1, n, 2):
        s = r*m+1
        row = list(range(s, s+m))
        ans.append(row)
    for r in ans:
        print(*r)
