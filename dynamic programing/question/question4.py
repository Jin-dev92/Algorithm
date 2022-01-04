import time

#   효율적인 화폐 구성
start = time.time()
# 입력 조건 - 첫번째 줄에 n,m 이 주어진다. (1 ~ 100 , 1~ 10000)
# 이후 n개의 줄에는 각 화폐의 가치가 주어진다. 화폐 가치는 1만보다 작거나 같은 자연수이다.
# 출력 조건 - 첫째줄에 m원을 만들기 위한 최소한의 화폐 개수를 출력
# 불가능할때는 -1 출력
n, m = map(int, input().split())
# data_lists = []
#
# for i in range(n):
#     data_lists.append(int(input()))

# data_lists.sort()
#
# d = [0] * len(data_lists)
# d[0] = m % data_lists[0]
# result = 0

# for i in range(1, len(data_lists)):
#     if m % data_lists[i] == 0:
#         result = m // data_lists[i]
#         break
#     d[i] = d[i - 1] % data_lists[i]
#     if d[i] == 0 and d[i - 1] == 0:
#         result = -1
#     elif d[i] == 0 and d[i - 1] != 0:
#         d[i] = d[i - 1] % data_lists[i]
#
# print(result)
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
print(time.time() - start)
