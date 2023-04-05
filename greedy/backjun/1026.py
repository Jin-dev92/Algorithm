n = int(input())
A, B = list(map(int, input().split())), list(map(int, input().split()))
A.sort()
B.sort(reverse=True)
s = 0
for i in range(n):
    s += A[i] * B[i]
print(s)
