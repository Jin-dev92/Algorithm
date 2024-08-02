
T = int(input())  # 테스트케이스
cached = [[0] * 15 for _ in range(15)]
for j in range(0, 14):
    for i in range(1, 15):
        if j == 0:
            cached[j][i] = i
        else:
            cached[j][i] = cached[j][i - 1] + cached[j - 1][i]

result = []
for i in range(T):
    K = int(input())
    N = int(input())
    result.append(cached[K][N])

for i in result:
    print(i)

