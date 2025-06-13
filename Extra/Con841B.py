for _ in range(int(input())):
    s = input()
    n = len(s)
    l = []
    for i, c in enumerate(s):
        if c == "0" or c == "1":
            l.append(c)
        else:
            if i > 0 and l[i-1] == '1':
                l.append('1')
            else:
                l.append('0')
    print(''.join(l))
