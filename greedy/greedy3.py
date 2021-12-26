# 1이 될때 까지
# 어떠한 수 n이 1이 될때까지 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 단, 두 번째 연산은 n이 k로 나누어 떨어질 때만 선택할수 있다.
# 1. n에서 1을 뺀다
# 2. n을 k로 나눈다.

n, k = map(int, input().split())
result = 0
# while n == 1:
#     if n % k == 0:
#         n /= k
#         print(n)
#         result = result + 1
#     else:
#         n = n - 1
#         result = result + 1
#
# print(result)
# n이 k 이상이라면 k로 계속 나누기
while n >= k:
    # N이 k로 나누어 떨어지지 안흔다면 n에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # k로 나누기
    n //= k
    result += 1
# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    print(n)
    n -= 1
    result += 1

print(result)
