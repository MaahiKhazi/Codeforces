n = int(input())
num = 0
for i in range(0, n):
    a = input()
    if a.count('1') >= 2:
        num += 1
print(num)

