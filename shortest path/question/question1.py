import time

# 미래 도시
program_start = time.time()

INF = int(1e9)
n, m = map(int, input().split())  # n 노드 갯수 , m 간선 갯수
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())  # x 소개팅 상대 위치 , k 중간에 거치는 곳
# 1 - k - x 목표
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k], graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("도달할수없음")
else:
    print(distance)

program_end = time.time() - program_start
print(program_end)
