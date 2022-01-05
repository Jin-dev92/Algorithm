# 다익스트라 최단 경로 알고리즘
# GPS 소프트웨어의 기본 알고리즘
# 알고리즘의 원리
# 1. 출발 노드를 설정
# 2. 최단 거리 테이블을 초기화
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
# 5. 위 과정에서 3과 4를 반복한다
# 다익스트라 알고리즘 구현 방법
# 1. 구현하기 쉽지만 느리게 동작하는 코드
# 2. 구현하기에 조금더 까다롭지만 빠르게 작동하는 소스
# 도달하지 못하는 노드는 무한 (1e9) 로 둔다.
# 한 단계 당 하나의 노드에 대한 최단 거리를 확실히 찾는 것
# 방법 1 . 간단한 다익스트라 알고리즘
# 단계마다 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인(순차 탐색) 한다.
# import sys
#
# input = sys.stdin.readline()
# INF = int(1e9)
# # 노드의 개수, 간선의 개수를 입력받기
# # n, m = map(int, input().split())
# n, m = map(int, input().split())
# # 시작 노드 번호를 입력받기
# start = int(input())
# # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
# graph = [[] for i in range(n + 1)]
# # 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
# visited = [False] * (n + 1)
# # 최단 거리 테이블을 모두 무한으로 초기화
# distance = [INF] * (n + 1)
#
# # 모든 간선 정보 입력 받기
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
#     graph[a].append(b, c)
#
#
# # 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
# def get_smallest_node():
#     min_value = INF
#     index = 0  # 가장 최단 거리가 짧은 노드(인덱스)
#     for i in range(1, n + 1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = 1
#     return index
#
#
# def dijkstra(start):
#     # 시작 노드에 대해서 초기화
#     distance[start] = 0
#     visited[start] = True
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
#     for i in range(n - 1):
#         now = get_smallest_node()
#         visited[now] = True
#         # 현재 노드와 연결된 다른 노드를 확인
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if cost < distance[j[0]]:
#                 distance[j[0]] = cost
#
#
# dijkstra(start)
#
# for i in range(1, n + 1):
#     # 모달 할수 없는 경우 무한 이라고 출력
#     if distance[i] == INF:
#         print("도달할수 없음")
#     else:
#         print(distance[i])

#   --------------------------------------------------------
# 방법 2. 개선된 다익스트라 알고리즘
# 힙 자료구조 - 우선순위 큐를 구현하기  위한 자료구조
# 우선순위가 가장 높은 데이터가 먼저 삭제되는 자료구조
# (가치, 물건) 식으로 데이터를 삽입하는데 '가치' 벨류가 우선순위 값이 된다.

import heapq
import sys
import time

start_time = time.time()
# input = sys.stdin.readline()
INF = int(1e9)
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하며, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면 계속 돌아감
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 수행
dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("도달할수 없음")
    else:
        print(distance[i])
print(time.time() - start_time)
