import math

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if i+1 == l[i]:
            c += 1
    print(c//2 + c%2)