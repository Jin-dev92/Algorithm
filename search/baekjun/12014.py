# case_count = int(input())
#
#
# def binary_search(arr, start, end):
#     buy_list = [arr[0]]
#     for i in range(1, len(arr) - 1):
#         if arr[i - 1] < arr[i]:  # 이 때 산다.
#             buy_list.append(arr[i])
#         else:
#             continue
#     if len(buy_list) >= k:
#         return 1
#     else:
#         return 0
#
#
# for count in range(case_count):
#     print("Case # {}".format(count + 1))
#     n, k = map(int, input().split())  # n = 날짜 , k = 주식  사는 횟수
#     array = list(map(int, input().split()))  # 각 날짜 별 주식 가격
#     print(binary_search(array, 0, n))
import sys

input = sys.stdin.readline


def binary_search(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if lis[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


test_case = int(input())

for tc in range(1, test_case + 1):
    N, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    lis = [numbers[0]]
    for i in range(1, N):
        if lis[-1] < numbers[i]:
            lis.append(numbers[i])
            print(lis)
            print(lis[-1])
        else:
            j = binary_search(0, len(lis) - 1, numbers[i])
            lis[j] = numbers[i]

    print('Case #{}'.format(tc))
    if len(lis) >= K:
        print(1)
    else:
        print(0)
