# 선택 정렬 : 매번 가장 작은 데이터를 선택해 맨 앞으로 보낸다
# 1. 전체 배열 안에서 가장 작은 수를 찾아 맨 앞으로 보낸다
# 2. 배열[0]을 제외하고 데이터중에서 가장 작은 데이터를 찾아 맨 앞으로 보낸다
# 무한 반복
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
            print(array)
    array[i], array[min_index] = array[min_index], array[i]  # swap