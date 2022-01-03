# 1로 만들기
# 정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.
# - X가 5로 나누어 떨어지면, 5로 나눈다.
# - X가 3으로 나누어 떨어지면 3으로 나눈다
# - X가 2로 나누어 떨어지면 2로 나눈거
# - X에서 1을 뺀다.
import time

start = time.time()
# X가 주어졋을 때 연산 4개를 적절히 사용하여 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
x = int(input())
# count = 0
# def calcultate(x):
#     global count
#     if x == 1:
#         return count
#     count += 1
#     if x % 5 == 0:
#         return calcultate(x // 5)
#     if x % 3 == 0:
#         return calcultate(x // 3)
#     if x % 2 == 0:
#         return calcultate(x - 1)
#
#
# print(calcultate(x))
# 메모라이징
d = [0] * 30001
for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
#
print(d[x])
print(time.time() - start)
# 3.0442583560943604 , x = 30000 기준 3.0442583560943604초 (메모라이징)
# 5.051976680755615 , x = 30000 기준 5.051976680755615초 (재귀)