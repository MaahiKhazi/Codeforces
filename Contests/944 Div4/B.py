for _ in range(int(input())):
    s = input()
    if len(set(s)) == 1:
        print('No')
    else:
        l = s[1:] + s[0]
        print('Yes')
        print(l)