import time

#   다익스트라 알고리즘 - 한 지점에서 다른 특점 지점까지의 최단 경로를 구하는 알고리즘
#   플로이드 워셜 알고리즘 - 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야하는 경우에 사용하는 알고리즘
program_started = time.time()
#   다이나믹 프로그래밍의 한 종류임 ( 점화식 찾기 )
#   각 단계에서는 해당 노드를 거쳐 가는 경우를 고려한다.
#   ex) 1번 노드에 대해 확인할 때는 1번 노드를 중간에 거쳐 지나가는 모든 경우를 고려한다. (A -> 1 -> B 비용을 확인후에 비용을 갱신)
#   현재 확인하고 있는 노드를 제외하고 , n-1 개의 노드 중에서 서로 다른 노드 (a,b)쌍을 선택하여 a -> 1 -> b 비용을 확인한 후에
#   비용을 확인 후 갱신
#   점화식 = Dab = min(Dab , Dak + Dkb)  / k - 중간에 거치는 노드 ( ab 거리와 a,k거리 + b,k거리 두개 비교)
#   자기자신은 0으로 해주고 도달하지 못하는 곳은 int(1e9)로 해준다.
INF = int(1e9)
n = int(input())  # 노드 갯수
m = int(input())  # 간선 갯수
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:  # 자기자신은 0
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할수 없는 경우
        if graph[a][b] == INF:
            print("도달할수없음")
        else:
            print(graph[a][b], end=" ")
print()
print(time.time() - program_started)
