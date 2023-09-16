import math

n, m, a = map(int, input().split())
ans = math.ceil(m/a) * math.ceil(n/a)
print(ans)
