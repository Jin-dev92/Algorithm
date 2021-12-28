from collections import deque


# stack
# 상자 쌓기에 비유할 수 있음.
# 기본적으로 배열을 선언하면 스택구조로 선언이 됨.
# stack = [4]
# stack.pop(4)

# queue
# 선입 선출
# queue = deque()
# queue.append(4)
# queue.pop()  # 오른쪽부터 제거
# queue.popleft()  # 왼쪽부터 제거
# queue.reverse()
# 5! = 5 * 4 * 3 * 2 * 1


# 재귀 함수 ( Recursive Function )
def recursive_functions(n): # 팩토리얼 재귀 함수 구현
    if n == 1:  # 무한 루프 탈출 조건
        return 1
    return n * recursive_functions(n - 1)  # 탈출 조건을 제시하지 않는 다면 에러가 뜬다.





# print(recursive_functions(5))
