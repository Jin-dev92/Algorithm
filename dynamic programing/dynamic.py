# 피보나치 수열
# 피보나치 수열은 동적 프로그래밍으로 처리 할 수 있다.
# 재귀 함수로 구현
def pibonacci(x):
    if x == 1 or x == 2:
        return 1
    return pibonacci(x - 1) + pibonacci(x - 2)


print(pibonacci(4))

# 위와 같이 재귀함수로 피보나치 수열을 작성한 경우, x의 숫자가 커지면 커질수록 러닝 타임이 기하급수적으로 늘어난다.
# 메모이제이션 기능을 사용하여 재귀함수를 구현
d = [0] * 100


# 0 1 1 2
def fibo(x):
    # 종료 조건
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:  # 계산한 적이 있다면
        return d[x]
    # 아직 계산히자 않은 문제라면 점화식에 따라 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    # d[x] = dx
    return d[x]


print(fibo(99))
