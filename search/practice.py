graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]
visited = [False] * 9
return_val = []

def bfs(graph, v, visited): # v 탐색 시작 지점
    # 이미 방문했었다면? 다른 걸 봐야하나
    visited[v] = True
    print(v,end=' ')
    for temp in graph[v]:
        if not visited[temp]:
            bfs(graph,temp,visited)


bfs(graph, 1, visited)
