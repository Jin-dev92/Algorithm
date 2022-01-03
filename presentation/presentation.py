# 110p 상하좌우 문제
# n = map(int, input().split())

# n = int(input())  # 배열 수 n * n
# move_input = input().split()  # 명렁 input
# move_types = ["L", "R", "U", "D"]
# dx = 1
# dy = 1
#
# for move in move_input:
#     if move == "L":  # 1.1 일때 왼 , 위 안됨.
#         if dx > 1:
#             dx -= 1
#         break
#     elif move == "R":
#         if dx != n:
#             dx += 1
#         break
#     elif move == "U":
#         if dy > 1:
#             dy += 1
#         break
#     elif move == "D":
#         if dy != n :
#             dy -= 1
#         break
#
# print(dy, dx)

n = int(input())
plans = input().split()
x, y = 1, 1

# L , R , U  , D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)
