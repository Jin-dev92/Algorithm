# 문제
# Day Of Mourning의 기타리스트 강토가 사용하는 기타에서 N개의 줄이 끊어졌다. 따라서 새로운 줄을 사거나 교체해야 한다. 강토는 되도록이면 돈을 적게 쓰려고 한다.
# 6줄 패키지를 살 수도 있고, 1개 또는 그 이상의 줄을 낱개로 살 수도 있다.
# 끊어진 기타줄의 개수 N과 기타줄 브랜드 M개가 주어지고, 각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의 가격, 낱개로 살 때의 가격이 주어질 때,
# 적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램을 작성하시오.

# 입력 첫째 줄에 N과 M이 주어진다. N은 100보다 작거나 같은 자연수이고,
# M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에는 각 브랜드의 패키지 가격과 낱개의 가격이 공백으로 구분하여 주어진다. 가격은 0보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

n, m = list(map(int, input().split()))
package_list = []
piece_list = []

for _ in range(m):
    package, piece = list(map(int, input().split()))
    package_list.append(package)
    piece_list.append(piece)
    # n : 끊어진 기타줄 갯수
    # m : 기타줄 브랜드 갯수
    # k : 브랜드 패키지 가격과 낱개 가격이 들어 있는 리스트
piece_list.sort()
package_list.sort()

if n < 6:
    if package_list[0] < piece_list[0] * n:
        print(package_list[0])
    else:
        print(n * piece_list[0])
else:  # 끊어진 게 6 이상일 경우
    min = 1e9
    for i in range((n // 6) + 1):
        # i = 패키지 갯수
        result = package_list[0] * i + piece_list[0] * (n - (i * 6))
        if min > result:
            min = result
    if min > (n // 6 + 1) * package_list[0]:
        print((n // 6 + 1) * package_list[0])
    else:
        print(min)
