# 시각
# 정수 n 입력시 00시 00분 00초 부터 n시 59분 59초까지의 모든 시간 중 3을 포함하고 있는 모든 경우의 수를 구하는 프로그램
n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1


print(count)