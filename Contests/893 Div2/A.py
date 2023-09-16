for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a > b:
        anna_advantage = True
    elif a < b:
        anna_advantage = False
    else:
        anna_advantage = (a + b + c) % 2 == 1
    if anna_advantage:
        print("First")
    else:
        print("Second")