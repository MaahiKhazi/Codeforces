for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = set(list(map(int, input().split())))
    b = set(list(map(int, input().split())))
    ca, cb = k//2, k//2
    flag = 1
    common = a.intersection(b)
    for i in range(1, k+1):
        if i in common:
            continue
        elif ca>0 and i in a:
            ca-=1
        elif cb>0 and i in b:
            cb-=1
        else:
            flag=0
            break
    if flag:
        print("YES")
    else:
        print("NO")
