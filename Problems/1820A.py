for _ in range(int(input())):
    s = input()
    ans = 0
    if s == "^":
        print(1)
        continue
    if s[0] == "_":
        ans += 1
    if s[len(s) - 1] == "_":
        ans += 1
    for i in range(len(s) - 1):
        if s[i] == '_' and s[i + 1] == "_":
            ans += 1
    print(ans)
