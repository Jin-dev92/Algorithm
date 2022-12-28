# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7],
# ]
# visited = [False] * 9
# return_val = []
#
# def bfs(graph, v, visited): # v 탐색 시작 지점
#     # 이미 방문했었다면? 다른 걸 봐야하나
#     visited[v] = True
#     print(v,end=' ')
#     for temp in graph[v]:
#         if not visited[temp]:
#             bfs(graph,temp,visited)
#
#
# bfs(graph, 1, visited)
# 4 6
# 19 15 10 17
import bisect

# 이진 탐색 연습 문제
# n, m = map(int, input().split())
# height = list(map(int, input().split()))
#
# start = 0
# end = max(height)
# result = 0
# while start <= end:
#     mid = (start + end) / 2
#     total = 0
#     for item in height:
#         if item > mid:
#             total += item - mid
#
#     if total < m : # 떡의 양이 부족한 경우 ?
#         end = mid - 1
#     else: # 충분한 경 덜 자르기 (오른쪽 탐색)
#         result = mid
#         start = mid + 1
#
# print(result)

# 이진 탐색
n, x = map(int, input().split())
array = list(map(int, input().split()))

print(bisect.bisect_right(array, x) - bisect.bisect_left(array, x))
