for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = 0
    j = 0
    i = 0
    while i<n and j<n:
        if a[i]<=b[j]:
            i+=1
            j+=1
        else:
            c+=1
            j+=1
    print(c)