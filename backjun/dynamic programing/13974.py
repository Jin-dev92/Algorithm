T = int(input())
for _ in range(T):
    K = int(input())
    data = list(map(int, input().split()))
    dp = [0] * len(data)
    dp[0] = data[0]

