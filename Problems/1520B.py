for _ in range(int(input())):
    n = int(input())
    count = 0
    power = 1
    while power <= n:
        for i in range(1, 10):
            if power * i <= n:
                count += 1
        power = power * 10 + 1
    print(count)
