# 두 배열의 원소 교체
# 동빈이는 최대 k 번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A의 원소와 B의 원소를 하나씩 골라서 두 원소를 바꾸는것. 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며, 여러분은 동빈이를 도와야한다.
# K 번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 a의 모든 원소의 합의 최댓값을 출력하는 프로그램을 만드세요

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break;
# def program(k):
#     sum = 0
#     sort_A = sorted(a)
#     sort_B = sorted(b, reverse=True)
#
#     for i in range(k):
#         sort_A[i], sort_B[i] = sort_B[i], sort_A[i]
#     for i in sort_A:
#         sum += i
#     return sum
#
#
# print(program(3))
