# # https://www.youtube.com/watch?v=liuUazQaLuU&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=32  1번 문제
# import heapq
#
# n, m, c = map(int, input().split())  # n = 도시의 개수 m = 통로의 개수 c= 메시지를 보내고자 하는 도시(시작점)
# graph = [[] for i in range(n + 1)]
# for _ in range(m):
#     start, end, cost = map(int, input().split())
#     graph[start].append((end, cost))
# INF = 1e9
# distance = [INF for _ in range(n + 1)]
#
#
# def dijkstra(start):
#     q = []
#     distance[start] = 0
#     heapq.heappush(q, (distance[start], start))  # 시작 지점을 넣는다. (비용, 노드)
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for temp in graph[now]:
#             cost = dist + temp[1]
#             if cost < distance[temp[0]]:
#                 distance[temp[0]] = cost
#                 heapq.heappush(q, (cost, temp[0]))
#
#
# dijkstra(c)
#
# count = 0
# for dist in distance:
#     if dist != INF:
#         count += 1
#
# print(count - 1, max([x for x in distance if not x == INF]), end=' ')

# 2 번 문제
n, m = map(int, input().split())
INF = 1e9
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0  # 자기 자신은 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())  # x = 최종 목적지 , k = 가는 길에 들러야 하는 곳

# 플로이드 워셜 점화식
for k in range(1, n + 1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)
# def washell(start):
#     for k in range(n):
#         for a in range(n):
#             for b in range(n):
#                 distance[a][b] = min(distance[a][b], distance[a][k] + distance[k][b])
#                 # graph[a][b]
#     print()
