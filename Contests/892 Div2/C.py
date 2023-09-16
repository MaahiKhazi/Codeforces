for _ in range(int(input())):
    n = int(input())
    a = ((n-2)*(n-1)*(2*n-3)) // 6
    ans = a + (n-1)*n
    print(ans)