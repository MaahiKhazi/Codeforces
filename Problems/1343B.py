for _ in range(int(input())):
    n = int(input())
    '''ans = []
    if n % 2 == 1:
        print('NO')
    else:
        if n % 4 != 0:
            print('NO')
        else:
            print('YES')
            for i in range(1, n+1):
                if i % 2 == 0:
                    ans.append(i)
                    es = sum(ans)
            for i in range(1, n-1):
                if i % 2 != 0:
                    ans.append(i)
                    ts = sum(ans)
            os = ts - es
            ts = es - os
            ans.append(ts)
            print(*ans)'''
    n //= 2
    if n & 1:
        print('NO')
        continue
    print('YES')
    for i in range(1, n+1):
        print(i*2, end=' ')
    for i in range(1, n):
        print((i*2)-1, end=' ')
    print(3 * n - 1)

