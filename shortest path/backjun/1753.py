# 문제
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.
#
# 입력
# 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다.
# 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.
# 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.
#
# 출력
# 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.
import heapq
import time
# st = time.time()

V, E = map(int, input().split())  # v = 정점의 개수, e = 간선의 개수
k = int(input())  # 시작 정점 번호
INF = int(1e9)
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
distance = [INF for _ in range(V + 1)]


def dijkstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (distance[start], start))
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for info in graph[now]:
            # 2,2 3,3
            dest, weight = info  # 도착지, 가중치
            cost = dist + weight
            if cost < distance[dest]:
                distance[dest] = cost
                heapq.heappush(queue, (cost, dest))

    for i in range(1, len(distance)):
        print(distance[i] if distance[i] != INF else 'INF')


dijkstra(k)
# print(time.time() - st)

# for i in range(1, len(distance)):
#     print(distance[i] if distance[i] != INF else 'INF')
