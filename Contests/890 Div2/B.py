for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    freq = {}
    
    for i in l:
        freq[i] = freq.get(i, 0) + 1
    
    flag = any(f > n // 2 for f in freq.values())
    
    if flag:
        print('NO')
    else:
        print('YES')
