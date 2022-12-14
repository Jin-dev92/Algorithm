# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
from collections import deque

n, m, v = list(map(int, input().split()))
path = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = tuple(map(int, input().split()))
    path[a].append(b)
    path[b].append(a)

visited = [False] * (n + 1)
dfs_list = []
bfs_list = []

def dfs(path, start, visited):  # 깊이 우선 탐색
    visited[start] = True
    dfs_list.append(str(start))
    path[start].sort()
    for temp in path[start]:
        if not visited[temp]:
            dfs(path, temp, visited)

def bfs(path, start):  # 너비 우선 탐색
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    while queue:
        v = queue.popleft()
        bfs_list.append(str(v))
        path[v].sort()
        for i in path[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(path, v, visited)
bfs(path, v)
print(' '.join(dfs_list))
print(' '.join(bfs_list))
