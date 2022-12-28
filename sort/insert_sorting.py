# 삽입 정렬
# 삽입 정렬은 두번째 부터 시작 ( 첫번째는 정렬되어있다고 판단)
# 두 번째 데이터인 5가 첫번째 데이터 기준으로 어떤 위치로 갈지 판단한다.
# 세 번째 데이터가 어떤 위치에 들어갈 지 판단한다. 삽입될 수 잇는 위치는 총 3가지이다.
# 반복.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(1, len(array)):
#     for j in range(i, 0, -1):
#         if array[j] < array[j - 1]:
#             array[j], array[j - 1] = array[j - 1], array[j]
#         else:
#             break
# print(array)
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            print(j)
            break

print(array)
