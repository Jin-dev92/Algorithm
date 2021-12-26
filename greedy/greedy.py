# 카운터에는 거스름돈으로 사용할 500원, 100원 , 50원 , 10원 짜리 동전이 무한히 존재한다고 가정 할 때 , 손님에게 거슬러 줘야 할 돈이 N원일 때 줘야 할 동전의 최소 갯수를 구하여라
def solution(n):
    result = 0
    coin_type = [500,100,50,10]
    for coin in coin_type :
        # print(n // coin) # 왼쪽에서 오른쪽으로 나눈 정수값을 구함
        result += (n // coin)
        n %= coin ## 연산자의 왼쪽 값에서 오른쪽 값을 나눈 값의 나머지를 왼쪽에 할당한다.
        # print(n)

    print(result)
    return result


solution(1260)