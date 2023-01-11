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

# Branch and Bound
'''
# N: The number of items / K: Maximnum weight
N, K = map(int,input().split())

weights = list()
values = list()

for _ in range(N):
    W, V = map(int,input().split())
    weights.append(W)
    values.append(V)

max_value = 0
find_value(0, 0, 0)
print(max_value)
'''
# Dynamic Programming
# N: The number of items / K: Maximnum weight
N, K = map(int,input().split())

dp = [0]*(K+1)

for idx in range(1, N+1):
    W, V = map(int,input().split())
    for i in range(K, W-1, -1):
        dp[i] = max(dp[i], dp[i-1], dp[i-W] + V)
    # print(f'--- DP\n{dp}\n')

print(dp[K])
