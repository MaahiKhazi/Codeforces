for _ in range(int(input())):
    s = input()
    n = len(s)
    l = ["?"]*n
    for i in range(n):
        if s[i] != "?":
            l[i] = s[i]
    print(l)


