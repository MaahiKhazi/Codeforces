# hoildays = [1, 6, 8, 21, 33]
# cost = [2, 7, 15]

# [1, 2, 3, 4, 6, 8 ,21, 33]
# [2, 7, 15]

# [1, 40, 44]
# [100, 5, 10]

# boxes = [[1], [2], [3], []] 

# boxes = [[1], [2, 3], [3], []]
# seen = []
# boxes = []
# n = int(input())
# for i in range(n):
#     keys = list(map(int, input().split()))
#     boxes.append(keys)
# seen = [0]
# for box in boxes:
#     for i in range(len(box)):
#         if box[i] not in seen:
#             seen.append(box[i])
# if len(seen) == n:
#     print("True")
# else:
#     print("False")
# keys= [1, 2, 3, 3]
# boxopen = [0, 1, 2, 3]

# ans = []
# opn = [0]
# i = 0
# ans.append(boxes[0][0])
# while 0 not in ans:
#     ans.append((boxes[ans[i]]))
#     opn.append(ans[i])
#     i += 1
# if len(opn) == n:
#     print("True")
# else:
#     print("False")


# def stairs(n):
#     dp = [0]*(n+1)
#     if n==0 or n == 1:
#         return 1
#     dp[0] = 1
#     dp[1] = 1
#     for i in range(2, n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n]

# n = int(input())
# print(stairs(n))

# for _ in range(int(input())):
#     n = int(input())
#     l = list(map(int, input().split()))
#     so, se = 0, 0
#     for i in range(n):
#         if i%2 == 0:
#             se = max(se, l[i])
#         else:
#             so = max(so, l[i])
#     se += (n+1)//2
#     so += n//2
#     print(max(se, so))


