for _ in range(int(input())):
    s = input()
    n = len(s)
    ans = '()'*n
    if s in ans:
        ans = '('*n + ')'*n
        if s in ans:
            print('NO')
        else:
            print('YES')
            print(ans)
    else:
        print('YES')
        print(ans)