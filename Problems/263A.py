a = []
for i in range(5):
	a.append([int(i) for i in input().split(' ')])
x, y = (0, 0)
for i in range(5):
	if a[i].count(1) > 0:
		y, x = (i, a[i].index(1))
print(abs(2-y)+abs(2-x))