N, M, K = map(int, input().split())
data = list(map(int, input().split()))
if len(data) != N:
    print("error")

data.sort()
first = data[N - 1]
second = data[N - 2]

result = first * (M // K) * K + second * (M % K)
# print(M // K)
print(result)
