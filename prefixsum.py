n, q = map(int, input().split())
a = list(map(int, input().split()))
pf = [0 for i in range(n)]
pf[0] = a[0]
for i in range(1, n):
    pf[i] = pf[i - 1] + a[i]
while q:
    l, r = map(int, input().split())
    print((pf[r] - pf[l - 1])//(r-l+1))
    q -= 1
