for _ in range(int(input())):
    q = int(input())
    l = list(map(int, input().split()))
    idx = 0
    ans = "1"
    flag = 0
    for i in range(1, q):
        if not flag and l[i] >= l[idx]:
            ans += "1"
            idx = i
        elif flag and l[i] >= l[idx]:
            if l[i] > l[0]:
                ans += "0"
            else:
                ans += "1"
                idx = i
        elif not flag and l[i] < l[idx]:
            if l[i] > l[0]:
                ans += "0"
            else:
                ans += "1"
                idx = i
                flag = 1
        elif flag and l[i] < l[idx]:
            ans += "0"
    print(ans)