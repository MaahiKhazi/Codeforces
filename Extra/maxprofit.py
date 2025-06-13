n = int(input())
l = list(map(int, input().split()))
ans = 0
res = 0
i = 0
j = 1
while j < len(l):
    ans = l[j] - l[i]
    if l[i] < l[j]:
        res = max(ans, res)
    else:
        i = j
    j += 1
print(res)
