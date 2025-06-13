for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    freq = {}
    ans = []
    for i in l:
        if i in freq:
            ans.append(chr(ord('a') + freq[i]))
            freq[i] += 1
        else:
            ans.append(chr(ord('a') + freq.get(i, 0)))
            freq[i] = 1
    print(''.join(ans))
    