for _ in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    if l.count(max(l, key=l.count)) < k:
        print(len(l))
    else:
        print(k-1)