for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    if len(set(l)) == 1:
        print("Alice")
    else:
        # mini = min(s)
        # if mini == 1:
        #     if len(s)%2 == 0:
        #         print("Bob")
        #     else:
        #         print("Alice")
        # else:
        #     print("Alice")
        while(len(l)>0):
            if len(l)%2 == 0:
                l = [elem - (min(l)-1) for elem in l]
            else:
                l = [elem - (min(l)) for elem in l]
        print(l)
        