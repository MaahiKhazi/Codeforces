for _ in range(int(input())):
    n, m = map(int, input().split())
    s = []
    value = 0
    for i in range(n):
        s.append(input())
    for i in range(len(s[0])):
        value += abs(ord(s[0][i]) - ord(s[1][i]))
    if n > 2:
        for p in range(n):
            for j in range(p+1, n):
                temp = 0
                for k in range(m):
                    temp += abs(ord(s[p][k]) - ord(s[j][k]))
                value = min(value, temp)
    print(value)

