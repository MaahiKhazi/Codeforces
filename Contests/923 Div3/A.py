for _ in range(int(input())):
    n = int(input())
    s = input()
    c = 0
    f = s.index('B')
    l = s.rfind('B')
    print(l-f+1)