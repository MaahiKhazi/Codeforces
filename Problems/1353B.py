for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())), reverse=True)
    ans = []
    '''for i in range(k):
        for j in range(n):
            if b[j] > a[j]:
                b[j], a[j] = a[j], b[j]
                break
    for i in range(n):
        max_sum += a[i]
    print(max_sum)'''
    for i in range(k):
        c = a[i]
        if a[i] < b[i]:
            a[i] = b[i]
            b[i] = c
    ans.append(sum(a))
    for i in ans:
        print(i)
