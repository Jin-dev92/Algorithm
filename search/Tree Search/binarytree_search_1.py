# 부품 찾기
# 부품 n 개가 있다 각 부품은 정수 형태의 고유한 번호가 있다.
# 손님이 m개 종류의 부품을 대량으로 구매하겠다며 당일날 견적서를 요청했다. 동빈이는 때를 놓치지 않고 손님이 문의한 부품 m개 종류를 모두 확인하여 견적서를 작성행햐ㅏㄴ다. 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자
def binary_search(array, start, end, target):  # 재귀 함수를 이용한 풀이
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            # result.append(array_n[mid])
            return mid
        elif array[mid] < target:
            binary_search(mid + 1, end, target)
        else:
            binary_search(start, mid - 1, target)
    return None


n = int(input())
array_n = list(map(int, input().split()))  # 전자매장 부품
m = int(input())
array_m = list(map(int, input().split()))  # 필요한 부품

array_n.sort()

for x in array_m:
    result = binary_search(array_n, 0, n - 1, x)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 계수 정렬식 풀이 방법
# n = int(input())
# array = [0] * 1000001
#
# for i in input().split():
#     array[int(i)] = 1
#
# m = int(input())
# x = list(map(int, input().split()))
# for i in x:
#     if array[i] == 1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# 집합 자료형 풀이
# n = int(input())
# array = set(map(int, input().split()))
#
# m = int(input())
# x = list(map(int, input().split()))
#
# for i in x:
#     if i in array:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')
