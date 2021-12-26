# 큰 수의 법칙
# 동빈이의 큰수의 법칙
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 m번 더하여 가장 큰 수를 만드는 법칙이다. 단 배열의 특정한 인덱스에 해당하는 수가 연속해서 k번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.
# 배열의 크기 N, 숫자가 더해지는 횟수 M , 그리고 k가 주여질 때 동빈이의 큰수의 법칙에 따른 결과를 출력하시오.
# 입력 조건 :
# 첫쨰 줄에 N(2<= N <= 1000) , M ( 1<= M <= 10,000 ), k(1 <= k <= 10,000) 의 자연수가 주어지며 , 각 자연수는 공백으로 구분한다.
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단 각각의 자연수는 1이상 10,000 이하의 수로 주어진다.
# 입력으로 주어지는 k 는 항상 m보다 작거나 같다.
# 출력 조건 :
# 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.
# def solution(n, m, k):
#     result = 0
#     count = 0
#     maxVal = n.sort(reverse=True)[0]  # 최대값
#     for i in range(m):
#         result += maxVal
#         if (i % k == 0):
#             maxVal = n.remove(maxVal).sort(reverse=True)[0]
#         count += 1
#     print(result)
#     return result
#
#
# solution([2, 4, 5, 4, 6], 8, 3)

# n,m,k 를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# n 개의 수를 공백으로 구붅하여 입력받기
data = list(map(int, input().split()))
data.sort()
first = data[n - 1]  # 가장 큰수
second = data[n - 2]  # 가장 작은수

result = 0

while True:
    for i in range(k):
        if m == 0:
            break;
        result += first
        m -= 1  # 더할때 마다 1씩 빼기
        if m == 0:
            break;
            result += second  # 두번째로 큰 수를 한번 더하기
            m -= 1

print(result)
