# sorted() # 병합정렬을 사용해서 만든 라이브러리

# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# array.sort()
# result = sorted(array)


# key 를 이용한 소스 코드
def setting(data):
    print(data)
    return data[1]


array = [('바나나', 2), ('사과', 5), ('당근', 3)]
result = sorted(array, key=setting)
print(result)