ans = 0
for _ in range(int(input())):
    s = input()
    if s[0] == '+' or s[1] == '+':
        ans += 1
    else:
        ans -= 1
print(ans)
