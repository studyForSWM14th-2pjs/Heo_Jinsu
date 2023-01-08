# N: The number of people
N = int(input())

# Cost: Time per person
cost = list(map(int, input().split()))

cost.sort()

total_time = 0
for idx in range(N):
    total_time += sum(cost[:idx+1])

print(total_time)