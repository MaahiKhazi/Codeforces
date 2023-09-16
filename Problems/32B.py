s = input()
n = len(s)
s2 = ""
i = 0
while i < n:
    if s[i] == '.':
        # print(0, end='')
        s2 += "0"

    if s[i] == '-' and s[i + 1] == '.':
        # print(1, end='')
        s2 += "1"
        i += 1

    if s[i] == '-' and s[i + 1] == '-':
        # print(2, end='')
        s2 += "2"
        i += 1

    i += 1
print(s2)
