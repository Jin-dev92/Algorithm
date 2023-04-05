# 문제
# n(1≤n≤1,000)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스가 있다.
# 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 그러면 A번째 도시에서 B번째 도시 까지 가는데 드는 최소비용과 경로를 출력하여라.
# 항상 시작점에서 도착점으로의 경로가 존재한다.
#
# 입력
# 첫째 줄에 도시의 개수 n(1≤n≤1,000)이 주어지고 둘째 줄에는 버스의 개수 m(1≤m≤100,000)이 주어진다. 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다.
# 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.
# 그리고 m+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다.
#
# 출력
# 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.
# 둘째 줄에는 그러한 최소 비용을 갖는 경로에 포함되어있는 도시의 개수를 출력한다. 출발 도시와 도착 도시도 포함한다.
# 셋째 줄에는 최소 비용을 갖는 경로를 방문하는 도시 순서대로 출력한다.
import heapq

INF = 1e9
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
start, end = map(int, input().split())

def dijkstra(s):
    distance[s] = 0
    queue = []
    heapq.heappush(queue, (distance[s], s))
    temp = [start]
    while queue:
        dist, now = heapq.heappop(queue)
        # 방문 하지 않은 경우만 처리
        if distance[now] < dist:
            continue
        for info in graph[now]:
            dest, cost = info
            total_cost = dist + cost
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if total_cost < distance[dest]:
                distance[dest] = total_cost
                heapq.heappush(queue, (distance[dest], dest))
                if temp.count(now) == 0:
                    temp.append(now)
    temp.append(end) # 지나온 경로에 도착지 추가
    print(distance[end]) # # 최소 비용
    print(len(temp)) # 지나온 경로 길이
    print(*temp) # 지나온 경료
dijkstra(start)
