n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n//2):
    ans += (a[i] + a[n - 1 - i]) * (a[i] + a[n - 1 - i])
print(ans)
