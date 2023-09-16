n, k = map(int, input().split())
a = list(map(int, input().split()))
count = 0
temp = a[k-1]
for i in range(0, len(a)):
    if a[i] >= temp and a[i] > 0:
        count += 1
print(count)