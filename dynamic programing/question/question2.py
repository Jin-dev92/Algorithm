import time

# 개미전사
start = time.time()
n = int(input())
array = list(map(int, input().split()))
# d = [0] * 100
# d[0] = 0
# d[1] = array[0]
# for i in range(2, n):
#     d[i] = array[i - 2] + array[i]
# print(max(d))

d = [0] * 100
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])
print(d[n - 1])
print(time.time() - start)
