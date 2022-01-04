import time

#
start = time.time()
tiles = [(1, 2), (2, 1), (2, 2)]
n = int(input())
# height = 2
# dx = [0] * n
# dy = [0] * n
# d = [dx, dy]
# for tile in tiles:
#     x = int(tile[0])
#     y = int(tile[1])
#
#     for i in range(x):
#         for j in range(y):
#             d[i][j] = 1
d = [0] * 1001
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = d[i - 1] + 2 * d[i - 2]
print(d[n] % 796796)
print(time.time() - start)
