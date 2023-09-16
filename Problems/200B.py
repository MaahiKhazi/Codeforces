n = int(input())
p = list(map(int, input().split()))
orange = sum(p)/100
per = orange/n
ans = per*100
print(ans)