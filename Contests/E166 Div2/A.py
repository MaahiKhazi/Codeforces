for _ in range(int(input())):
    n = int(input())
    s = input()
    d = []
    l = []
    cl = 0
    ans = 1
    for c in s:
        if c.isdigit():
            d.append(c)
            if cl:
                ans = 0 
        elif c.isalpha():
            l.append(c)
            cl = 1
    if d!=sorted(d):
        ans = 0
    if l!=sorted(l):
        ans = 0
    if ans:
        print("YES")
    else:
        print("NO")
