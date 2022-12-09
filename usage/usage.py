import heapq
import sys
from bisect import bisect_left, bisect_right
from collections import deque, Counter
from itertools import permutations, combinations, product, combinations_with_replacement

a = 100
b = 11
c = 5
d = 3
# print(a // b)  # 몫 연산자
# print(c ** d)  # 제곱 연산자
#### 리스트 ###
n = 10
a = [0] * n
# print(a)  # 모든 값 0으로 초기화
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[1:4])  # index 1 ~ 4 출력 [시작 인덱스 : 끝 인덱스 - 1]
# 리스트 컴프리헨션 - 리스트를 초기화하는 방법.
arr = [i for i in range(20) if i % 2 == 1]  # 0 ~ 20 사이 홀수들만
# print(arr)
n = 2
m = 3
arr = [[0] * m for _ in range(n)]  # 2차원 배열 초기화
# _ 의 사용 -> index 값이 필요 없을 경우에
# print(arr)
arr = []


# arr.append('a')
# arr.insert('a',1) # insert(item, index)
# arr.remove(item)
# insert 는 공간 복잡도가 O(n) 이므로 append 의 공간 복잡도 (O(1)) 보다 높으므로 정말 필요할 경우에만 사용하도록 하자.

# 튜플
# 튜플은 리스트와 달리 한번 선언 한 후에 수정이 불가하다.
# 튜플은 ()로 선언한다.
# 최단 경로 알고리즘에서 많이 사용한다. 각

# 사전 자료형(dict) key-value 로 이루어져있고, 내부적으로 해쉬 테이블로 작동한다.
# 집합 (set) - 중복을 허용하지 않는다.
#           - 순서가 없다.
#           - {1,2,3}

# print(list(map(int, input().split(","))))
# map(적용시킬 함수, 적용할 값들(자료형)) , list, 튜플 집합 등의 자료형의 각각의 요소에 함수를 적용시킨다.
# n ,m, k = map(int, input().split())
# print(n,m,k)
# sys.stdin.readline().rstrip()

# 순열
# print(list(permutations(['a', 'b', 'c'], 3)))
# 조합
# print(list(combinations(['a', 'b', 'c'], 2)))
# product - 순열과 같지만 원소를 중복해서 뽑는다.
# print(list(product(['a', 'b', 'c'], repeat=2))) # 2개를 뽑는 모든 순열 , 중복을 허용한다.
# combinations_with_replacement - 조합과 같지만 원소를 중복해서 뽑는다.
# print(list(combinations_with_replacement(['a', 'b', 'c'], 2))) # 중복을 허용하는 모든 조합
# heapq (힙) - 우선순위 큐 , 원소를 삽입할 때는 heapq.heappush()를 사용하고, 힙에서 원소를 꺼낼때는 heapq.heappop() , 주로 최단 거리 알고리즘을 구할 떄 사용한다.

def heapsort__desc(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    print(f"h : {h}")
    for _ in range(len(h)):
        result.append(heapq.heappop(
            h))  # 정렬이 되네? -> 파이썬의 힙은 최소 힙으로 굿겅 되어있으므로 단순히 원소를 힙에 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN) 에 오름차순 정렬이 완료된다.
        print(f"h : {h}")
        print(f"result : {result}")


def heapsort__asc(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    print(f"h : {h}")
    for _ in range(len(h)):
        result.append(-heapq.heappop(
            h))  # 정렬이 되네? -> 파이썬의 힙은 최소 힙으로 굿겅 되어있으므로 단순히 원소를 힙에 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN) 에 오름차순 정렬이 완료된다.
        print(f"h : {h}")
        print(f"result : {result}")


# heapsort__desc([1,5,3,9,6,7])
# heapsort__asc([1,5,3,9,6,7])

# 이진 탐색
# - 정렬된 배열에서 특정 원소를 찾아야할 때 사용한다. 시간 복잡도 O(logN)
# print(bisect_left([1,2,4,5,8], 4)) # 정렬된 순서를 유지하며, 리스트 a 에 데이터 x 를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# print(bisect_right([1,2,4,5,8], 4)) # 정렬된 순서를 유지하며, 리스트 a 에 데이터 x 를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
# 값이 [left , right ] 사이에 존재하는 데이터의 개수를 반환하는 함수
def count_by_range(a, left, right):
    left_index = bisect_left(a, left)
    right_index = bisect_right(a, right)
    return right_index - left_index


# a = [1, 2, 3, 3, 3, 4, 4, 8, 9]
# print(count_by_range(a, 3, 3))  # 3의 갯수
# print(count_by_range(a, -1, 3))  # -1 , 3 사이의 숫자 갯수

# deque  ,
# 파이썬에 Queue 라이브러리가 있는데 이건 queue 구현 라이브러리가 아님. deque 로 구현해야됨.
# 양방향 큐 , 가장 앞,뒤 원소를 넣거나 제거할 때 O(1)
# deque.popleft()
# deque.pop()
# deque.appendleft() # 가장 왼쪽에 삽입
# deque.append() # 가장 오른쪽에 삽입

# counter 등장 횟수를 세어주는 라이브러리
# counter = Counter(['red','blue','red','blue','blue','green'])
# print(counter['blue'])
# print(dict(counter))
n = int(input())
# 숫자 입력 1 부터 n 까지 짝수만 더하여 출력
# count = 0
# for value in range(n + 1):
#     if value % 2 == 1:
#         continue
#     else:
#         print(value)
#         count += value
#
# print(count)
#