# # dp = [0 for _ in range(100)]
# # dp = [0] * 100
# # 탑다운
# # 1 1 2 3 5 8 13
# # def fibo(x):
# #     if x == 1 or x == 2:  # 종료 조건
# #         return 1
# #     # 이미 계산 되었을때
# #     if dp[x] != 0:
# #         return dp[x]
# #     dp[x] = fibo(x - 1) + fibo(x - 2)
# #     return dp[x]
#
# # print(fibo(99))
# # dp = [0] * 100
# # dp[1] = 1
# # dp[2] = 1
# # n = 99
# # for i in range(3, n + 1):
# #     dp[i] = dp[i - 1] + dp[i - 2]
#
#
# # x = int(input())
# # dp = [0] * (x + 1)
# # for i in range(2, x + 1):
# #     dp[i] = dp[i - 1] + 1
# #     if i % 2 == 0:
# #         dp[i] = min(dp[i], dp[i // 2] + 1)
# #     if i % 3 == 0:
# #         dp[i] = min(dp[i], dp[i // 3] + 1)
# #     if i % 5 == 0:
# #         dp[i] = min(dp[i], dp[i // 5] + 1)
# #
# # print(dp)
#
# # n, m = map(int, input().split())  # n = 화폐 종류 갯수, m = 주어진 금액
# # lis = []
# # for _ in range(n):
# #     lis.append(int(input()))
# # INF = 10001
# # d = [INF] * (m + 1)
# #
# # d[0] = 0
# # for i in range(n): # 각 화폐 마다 체크 한다.
# #     for j in range(lis[i], m + 1):
# #         if d[j - lis[i]] != INF: # i-k 을 만드는 방법이 존재하는 경우
# #             d[j] = min(d[j], d[j - lis[i]] + 1)
# #
# # if d[m] == INF:
# #     print(-1)
# # else:
# #     print(d[m])
# # print(d)
#
# T = int(input())
# for _ in range(T):
#     n, m = map(int, input().split())
#     array = list(map(int, input().split()))
#     dp = []
#     index = 0
#     for i in range(n):
#         dp.append(array[index:index + m])
#         index += m
#
#     for i in range(1, m):
#         for j in range(n):
#             top_case = dp[i - 1][j - 1] if j > 0 else 0
#             mid_case = dp[i - 1][j]
#             bottom_case = dp[i + 1][j - 1] if j == m else 0
#             # print("top_case {}".format(top_case))
#             # print("mid_case {}".format(mid_case))
#             # print("bottom_case {}".format(bottom_case))
#             dp[i][j] += max(top_case, mid_case, bottom_case)
#
#
#     print(dp)
# 가장 긴 증가하는 부분 수열(LIS)
# LIS 점화식 : d[i] = max(d[i],d[i-1]+1) if array[i-1] < array[i] # d[i]를 가장 마지막 원소로 갖는 부분 수열의 최대 길이
n = int(input())
lis = list(map(int, input().split()))
# dp = [0 for _ in range(n)]
# for i in range(1, n):
#     if dp[i - 1] != 0:
#         dp[i] = dp[i - 1]
#     if lis[i] > lis[i - 1]:
#         dp[i] += 1
#
# print(max(dp))

lis.reverse()
dp = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if lis[j] < lis[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n-max(dp))
