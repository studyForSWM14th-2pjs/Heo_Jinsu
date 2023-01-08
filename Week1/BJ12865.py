# Branch and Bound
def find_value(weight, value, idx):
    global N, K, weights, values, max_value

    # print(f'\nCurrent Weight: {weight}')
    # print(f'Current Value: {value}')
    # print(f'Current Index: {idx}')

    if weight <= K and value > max_value:
        # print('Max Value Changed!')
        max_value = value

    if weight > K or idx >= N:
        return 0
    else:
        find_value(weight + weights[idx], value + values[idx], idx + 1)
        find_value(weight, value, idx + 1)

# N: The number of items / K: Maximnum weight
N, K = map(int,input().split())

weights = list()
values = list()
# W: Weight of the item / V: Value of the item
for _ in range(N):
    W, V = map(int,input().split())

    weights.append(W)
    values.append(V)

max_value = 0

for idx in range(N):
    weight = 0
    value = 0

    # print(f'\nCurrent Index: {idx}')
    
    # print(j, weight, value)

    if value > max_value:
        max_value = value

print(max_value)