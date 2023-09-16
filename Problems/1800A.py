for _ in range(int(input())):
    n = int(input())
    s = input()
    if s[0] != "M" and s[0] != "m":
        print('No')
    else:
        s = s.lower()
        t = ""
        for i in s:
            if t == '':
                t += i
            elif t[-1] != i:
                t += i
        if t == "meow":
            print('Yes')
        else:
            print('No')

