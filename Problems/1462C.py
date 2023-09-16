for _ in range(int(input())):
    x = int(input())
    ans = []
    n = x
    sum_ = 0
    last = 9
    if x < 10:
        print(x)
    elif x > 45:
        print(-1)
    else:
        while n != sum_:
            if (n - sum_) > last:
                sum_ += last
                ans.append(last)
                last -= 1
            else:
                ans.append(n-sum_)
                sum_ = n
        ans.reverse()
        for i in range(len(ans)):
            print(ans[i], end='')
        print('')

