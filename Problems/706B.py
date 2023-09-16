from bisect import bisect

n = int(input())
x = list(map(int, input().split()))
x.sort()
q = int(input())
ans = 0
for i in range(q):
    m = int(input())
    ans = bisect(x, m, 0, n)
    print(ans)
