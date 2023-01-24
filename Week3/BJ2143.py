T = int(input())
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

dp1 = [0]*abs(T)
dp2 = [0]*abs(T)

for i in range(N):
    for j in range(i+1,N+1):
        temp = sum(A[i:j])
        if temp < T:
            dp1[temp] += 1

for i in range(M):
    for j in range(i+1,M+1):
        temp = sum(B[i:j])
        if temp < T:
            dp2[temp] += 1

method_num = 0
for i in range(1,T):
    method_num += dp1[i] * dp2[T-i]
print(method_num)

# T가 음수인 경우...