# n = int(input())
# a = 0.4 * n
# b = 0.16 * n
# e = 0.12 * a
# x = a + b + e
# #f = 0.0325 * x
# #c = n - (a+b+e+f)
# c = 0.3643*n
# d = a + b + c
# f = 0.0325 * d
# g = e + f
# total = g + d
# print(a, b, c, d, e, f, g, total)

def towers_of_hanoi(n, s, d, t):
    if n==1:
        print("Move disk ", n, "from ", s, "to ", d)
        return
    towers_of_hanoi(n-1, s, t, d)
    print("Move disk ", n, "from ", s, "to ", d)
    towers_of_hanoi(n-1, t, d, s)
    
n = int(input())
towers_of_hanoi(n, 'A', 'C', 'B')
