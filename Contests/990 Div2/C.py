for _ in range(int(input())):
    n = 2
    m = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    columns = list(zip(a, b))
    columns.sort(key=lambda x: (x[0], x[1]), reverse=True)
    sorted_matrix = list(zip(*columns))
    def compute_dp(matrix):
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = matrix[0][0]
        for j in range(1, m):
            dp[0][j] = dp[0][j-1] + matrix[0][j]
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + matrix[i][0]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = matrix[i][j] + max(dp[i-1][j], dp[i][j-1])
        return dp[n-1][m-1]
    print(compute_dp(sorted_matrix))
    