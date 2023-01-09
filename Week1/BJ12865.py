# Branch and Bound
def find_value(weight, value, idx):
    global N, K, weights, values, max_value

    # print(f'\nCurrent Weight: {weight}')
    # print(f'Current Value: {value}')
    # print(f'Current Index: {idx}')
    
    if weight <= K and value > max_value:
        # print('Max Value Changed!')
        max_value = value

    if checking(weight, idx):
        find_value(weight + weights[idx], value + values[idx], idx + 1)
        find_value(weight, value, idx + 1)

def checking(weight, idx):
    global N, K, weights
    
    if idx >= N:
        return False
        
    for i in range(N):
        if i != idx-1 and  weights[i] <= K - weight:
            return True
    
    return False

# N: The number of items / K: Maximnum weight
N, K = map(int,input().split())

dp = [[0]*(K+1) for _ in range(N+1)]

for idx in range(1, N+1):
    W, V = map(int,input().split())
    for i in range(1, K+1):
        dp[idx][i] = max(dp[idx][i], dp[idx-1][i], dp[idx][i-1])
        if i >= W:
            dp[idx][i] = max(dp[idx][i], dp[idx-1][i-W] + V)

print(dp[N][K])