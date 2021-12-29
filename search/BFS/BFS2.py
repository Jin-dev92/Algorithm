# 미로 탈출 BFS 큐를 이용해 풀이한다.
# 동빈 위치 (1.1) 미로 출구는 (n , m ) 한번에 한칸씩,
# 괴물이 있는 부분 0 , 없는 부분 1 미로는 탈출할수 있는 형태,
# 동빈이가 탈출하기 위해 움직여야하는 최소 칸의 수 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

from collections import deque

n, m = map(int, input().split())  # n x m 크기
map_data = []  # 맵 데이터 세팅
for _ in range(n):
    map_data.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때 까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물인 경우 무시
            if map_data[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문 하는 경우에만 최단 거리 기록
            if map_data[nx][ny] == 1:
                map_data[nx][ny] = map_data[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return map_data[n - 1][m - 1]


print(bfs(0, 0))
