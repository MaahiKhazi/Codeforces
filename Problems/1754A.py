for _ in range(int(input())):
    n = int(input())
    s = input()
    a = 0
    for i in range(n):
        if s[i] == 'Q':
            a += 1
        elif s[i] == 'A':
            a -= 1
        if a < 0:
            a = 0
    if a == 0:
        print('Yes')
    else:
        print('No')
