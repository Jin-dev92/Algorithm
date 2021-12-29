# 퀵 정렬
# 가장 많이 사용되는 정렬 알고리즘
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿔준다.
# 기준을 설정한 다음 큰수와 작은수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다.
# 퀵 정렬에서는 피벗이 사용된다. 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 '기준'을 바로 피벗(리스트에서 첫번째 데이터) 이라고 한다.
# 피벗 설정 후에 왼쪽부터 피벗보다 큰 데이터를 찾고 오른쪽부터 피벗보다 작은 데이터를 찾는다. 그 다음 큰 데이터와 작은 데이터의 서로 위치를 교환해준다.
# 작업 후에는 피벗보다 작은 데이터들은 왼쪽으로 , 큰 데이터들은 오른쪽으로 가게 된다.
# 이후 , 2개의 파티션 내에서 각각 퀵 정렬을 실행한다.
# 아래 예시는 널리 알려진 풀이법이다.
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우엔 종료
        return
    pivot = start  # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)
# def quick_sorting(partition):
#     pivot = partition[0]
#     left_partition = []
#     right_partition = []
#     temp = []
#     for i in range(1, len(partition)):
#         if pivot > partition[i]:
#             left_partition.append(partition[i])
#         else:
#             right_partition.append(partition[i])
#     temp.append(left_partition)
#     temp.append(pivot)
#     temp.append(right_partition)
#     # temp.append(pivot)
#
#     return temp


# print(quick_sorting(array))
