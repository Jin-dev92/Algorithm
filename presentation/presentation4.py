# 게임 개발
# 1. 캐릭터가 보는 방향 왼쪽부터 갈곳을 정함.
# 2. 캐릭터 바로 왼쪽 방향에 아직 가보지 않은 칸이 있다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한칸 전진 없다면, 왼쪽방향으로 회전만 수행후 1단계로
# 3. 네 방향 모두 이미 가본 칸이거나 바다로 되어있는 칸인 경우, 바라보는 방향을 유지한 채로 한칸 뒤로 가고 1단계로 돌아간다. 단 , 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈수 없는 경우에는 움직임이 멈춘다.

# n, m = map(int, input().split())  # 세로 가로 길이
# a, b, d = map(int, input().split())  # a , b 캐릭터 좌표 , d 캐릭터 보는 방향 0,1,2,3 - 북동남서
# map_data = []
# character_moved_log = []
# dictionary = {
#     {
#         'left': map_data[a - 1][b],
#         'top': map_data[a][b - 1],
#         'right': map_data[a + 1][b],
#         'bottom': map_data[a][b + 1],
#     },
#     {
#         'left': map_data[a][b - 1],
#         'top': map_data[a + 1][b],
#         'right': map_data[a][b + 1],
#         'bottom': map_data[a - 1][b],
#     },
#     {
#         'left': map_data[a + 1][b],
#         'top': map_data[a][b + 1],
#         'right': map_data[a - 1][b],
#         'bottom': map_data[a - 1][b],
#     },
#     {
#         'left': map_data[a][b + 1],
#         'top': map_data[a - 1][b],
#         'right': map_data[a - 1][b],
#         'bottom': map_data[a - 1][b],
#     },
# }
# for i in range(n):
#     map_data.insert(i, tuple(map(int, input().split())))
#
#
# def character_move():
#
#
#     break;
#
# # 캐릭터 로그 쌓기
#
# print(map_data)
# # step = []


n, m = map(int, input().split())  # 세로 가로 길이
# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재 좌표 방문 처리

map_data = []
for i in range(n):
    map_data.append(list(map(int, input().split())))

# 북 , 동 , 남 , 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and map_data[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 못 갈 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈수 없다면 이동하기
        if map_data[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)