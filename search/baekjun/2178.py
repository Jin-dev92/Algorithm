# # 문제
# # 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
# # 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
# # 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
# # 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
from collections import deque

# # 입력
# # 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.
#
# # 출력
# # 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
#
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input()))))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, -1]
# 상 우 하 좌
queue = deque([(0, 0)])
visited = [(0, 0)]

while queue:
    target = queue.popleft()
    for index in range(4):
        if target[0] + dx[index] < 0 or target[1] + dy[index] < 0:
            print('길이 업슴')
            continue
        else:
            forward = (target[0] + dx[index], target[1] + dy[index])
            if forward not in visited and graph[forward[0]][forward[1]] == 1:
                print('{} 로 이동'.format(forward))
                queue.append(forward)
                visited.append(forward)
