for _ in range(int(input())):
    s1, s2 = map(str(), input().split())
    if len(s1) > len(s2):
        s1, s2 = s2, s1 
    s1 = '0'*(len(s2)-len(s1)) + s1
    