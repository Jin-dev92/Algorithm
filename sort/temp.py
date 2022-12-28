# array = [5, 9, 2, 6, 4, 8, 3, 7, 1]

# quick_sort practice

# def quick_sort(array, start, end):
#     pivot = start
#     left_side = start + 1
#     right_side = end
#     while left_side <= right_side:
#         while left_side <= end and array[pivot] >= array[left_side]:  # leftside 피벗 보다 작은 값
#             left_side += 1
#         while right_side > start and array[pivot] <= array[right_side]:
#             right_side -= 1
#
#         if right_side < left_side:
#             array[pivot], array[right_side] = array[right_side], array[pivot]
#         else:
#             array[left_side], array[right_side] = array[right_side], array[left_side]
#             print(array)
#
#     quick_sort(array, start, right_side - 1)
#     quick_sort(array, right_side+1, end)
#
# quick_sort(array, 0, len(array) - 1)

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     pivot = array[0]
#     tail = array[1:]
#     left_side = [x for x in tail if x <= pivot] # pivot 보다 작은 수
#     right_side = [x for x in tail if x > pivot] # pivot 보다 작은 수
#
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)
#
# print(quick_sort(array))

# 계수 정렬
# array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# index_list = [0 for _ in range(10)]
# for i in array:
#     index_list[i - 1] += 1
#
# for i in range(len(index_list)):
#     for j in range(index_list[i]):
#         print(i, end=' ')
