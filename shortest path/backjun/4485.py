# 문제
#
# 하여튼 젤다...아니 링크는 이 동굴의 반대편 출구, 제일 오른쪽 아래 칸인 [N-1][N-1]까지 이동해야 한다. 동굴의 각 칸마다 도둑루피가 있는데, 이 칸을 지나면 해당 도둑루피의 크기만큼 소지금을 잃게 된다. 링크는 잃는 금액을 최소로 하여 동굴 건너편까지 이동해야 하며, 한 번에 상하좌우 인접한 곳으로 1칸씩 이동할 수 있다.
#
# 링크가 잃을 수밖에 없는 최소 금액은 얼마일까?
#
# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
#
# 각 테스트 케이스의 첫째 줄에는 동굴의 크기를 나타내는 정수 N이 주어진다. (2 ≤ N ≤ 125) N = 0인 입력이 주어지면 전체 입력이 종료된다.
#
# 이어서 N개의 줄에 걸쳐 동굴의 각 칸에 있는 도둑루피의 크기가 공백으로 구분되어 차례대로 주어진다. 도둑루피의 크기가 k면 이 칸을 지나면 k루피를 잃는다는 뜻이다.
# 여기서 주어지는 모든 정수는 0 이상 9 이하인 한 자리 수다.
#
# 출력
# 각 테스트 케이스마다 한 줄에 걸쳐 정답을 형식에 맞춰서 출력한다. 형식은 예제 출력을 참고하시오.
import heapq


def dijkstra(s, cnt):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = []
    luffy[0][0] = graph[0][0]
    heapq.heappush(queue, (graph[0][0], s))
    while queue:
        amount, location = heapq.heappop(queue)
        if luffy[location[1]][location[0]] != INF:  # 방문한 적이 있을 경우에
            continue
        for i in range(4):
            x = dx[i] + location[1]
            y = dy[i] + location[0]
            if x < 0 or x > n or y < 0 or y > n:  # 올바르지 않은 인덱스인 경우
                continue
            luffy[y][x] = luffy[location[1]][location[0]] + graph[y][x]
            heapq.heappush(queue, (luffy[y][x], (x, y)))

        print("Problem", cnt, ":", luffy[-1][-1])


cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = []
    INF = 1e9
    luffy = [[INF for _ in range(n)] for _ in range(n)]
    start = (0, 0)
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    dijkstra(start, cnt)
