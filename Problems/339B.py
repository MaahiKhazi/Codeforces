n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
s = 1
for i in range(m):
    if a[i] >= s:
        ans += a[i] - s
    else:
        ans += n - (s - a[i])
    s = a[i]
print(ans)

