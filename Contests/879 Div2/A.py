import math

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    a = l.count(1)
    b = l.count(-1)
    ans = max((b - a + 1)//2, 0)
    b -= ans
    if b % 2 != 0:
        ans += 1
    print(ans)
    