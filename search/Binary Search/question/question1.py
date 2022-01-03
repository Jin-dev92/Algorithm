# 떡볶이 떡 만들기
n, m = map(int, input().split())
data_list = list(map(int, input().split()))
data_list.sort()


def solution():
    max = data_list[n - 1]
    min = 0
    # while True:
    for i in range(max, min, -1):
        count = 0
        for data in data_list:
            if data > i:
                count += data - i
        if count >= 6:
            return i


print(solution())

# 전형적인 이진 탐색 문제. 파라메트릭 서치 유형의 문제이다.
# 파라메트릭 서치 최적화 문제는 결정 문제로 바꾸어 해결하는 기법이다. ( 예 아니오로 대답 )
start = 0
end = max(data_list)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in data_list:
        if x > mid:
            total += x - mid
        # 떡 양이 부족 한 경우 더 많이 자르기
        if total < m:
            end = mid - 1
        # 떡의 양이 충분한 경우 덜 짜르기
        else:
            result = mid
            start = mid + 1
