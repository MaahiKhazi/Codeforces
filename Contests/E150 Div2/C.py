for _ in range(int(input())):
    s = input()
    d = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4}
    pre = [ [ 0 for i in range(len(s))] for j in range(5)]
    suf = [ 0 for i in range(len(s))]
    maxi = 0
    for i in range(len(s)-1, -1, -1):
        maxi = max(maxi, d[s[i]])
        suf[i] = maxi
    maxgain = 0
    for j in range(len(s)):
        for i in range(5):
            gain = 0
            pre[i][j] += pre[i][j-1] + (d[s[j]] == i)*(10**i)
    for i in range(5):
        for j in range(len(s)):
            pre[i][j] += pre[i-1][j]
    for j in range(len(s)):
        for i in range(5):
            if d[s[j]]==i:
                continue
            if d[s[j]]>=suf[j]:
                gain -= 10**d[s[j]]
            else:
                gain += 10**d[s[j]]
            if i >= suf[j]:
                gain += 10**i
            else:
                gain -= 10**i
    
            
    # print(suf)
    for row in pre:
        print(*row)
