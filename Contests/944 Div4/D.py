for _ in range(int(input())):
    s = input()
    ss = ''.join(sorted(s))
    if s==ss:
        print(1)
    else:
        co = []
        o = []
        for i in s:
            if i == '1':
                o.append(i)
            else:
                if o:
                    co.append(o)
                o = []
        print(len(co) + 1)