import math

for _ in range(int(input())):
    n, k = map(int, input().split())
    if k == 1:
        print(n)
    elif n == k:
        print(2)
    elif n % k == 1:
        print(math.ceil(n/k))
    else:
        print(math.ceil(n/k) + 1)
