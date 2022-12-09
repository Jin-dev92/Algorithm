import sys
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