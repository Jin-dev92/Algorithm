# BFS (Breadth First Search) 너비 우선 검색 -> 가까운 노드부터 탐색하는 알고리즘이다. 큐 구조에 넣은 게 일반적인 방법.
# 알고리즘의 작동 방식
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
# 3. 2번 과정을 더이상 수행할 수 없을 때 까지 반복한다.
from collections import deque

# deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
visited = [False] * len(graph)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 봅아 출력
        v = queue.popleft()
        print(v,end=' ')
        # 해당 원소와 연결되었고 , 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v] :
            if not visited[i]:
                queue.append(i)
                visited[i] = True



# 정의된 BFS 함수 호출
bfs(graph, 1, visited)