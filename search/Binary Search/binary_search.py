# 이진 탐색 - 배열 내부의 데이터가 정렬 되어있어야만 사용할 수 있는 알고리즘이다.
# 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교.


# array = []
def binary_search(array, target, start, end):
    if start > end:
        return None
    middle = (start + end) // 2
    if array[middle] == target:
        return middle
    elif array[middle] > target:
        return binary_search(array, target, start, middle - 1)
    else:
        return binary_search(array, target, middle + 1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split())).sort()

result = binary_search(array, target, 0, n - 1)
if result is None:
    print("찾는값 없음")
else:
    print(result + 1)
