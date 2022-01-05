import sys
import time
import heapq

# 전보
program_start = time.time()
# 프로그램 시작 다익스트라 알고리즘
# input = sys.stdin.readline()
INF = int(1e9)
n, m, start = map(int, input().split())  # n - 도시 갯수 m - 통로의 갯수 c - 메시지를 보내고자 하는 도시
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(queue)
        # print("dist", dist)
        # print("now", now)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인한다
        for i in graph[now]:
            cost = dist + i[1]  # 위에 있는 변수 z를 의미 즉, 코스트를 의미
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                # heapq.heappush((queue, (cost, i[0])))
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)

# 도달 할 수 있는 노드의 갯수
count = 0
# 도달할 수 있는 노드 중에서 , 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count - 1 출력
print(count - 1, max_distance)

print(time.time() - program_start)
