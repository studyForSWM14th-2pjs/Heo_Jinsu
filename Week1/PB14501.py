def possible_cons(cons_table, start, end):
    possible = list()

    for i in range(start, end):
        if i + cons_table[i][0] <= end:
            possible.append(i)
    
    return possible

def find_cost(cons_table: list, cost, start, end):
    global max_cost
    
    if start + cons_table[start][0] <= end:
        # print(f'\nStart Index: {start}, End Index: {end}')
        current_cost = cost + cons_table[start][1]
        # print(f'Cost: {current_cost}')
        possible = possible_cons(cons_table, start + cons_table[start][0], N)
        # print(f'Possible: {possible}')
        
        if len(possible) <= 0:
            if max_cost < current_cost:
                max_cost = current_cost
        else:
            while len(possible) > 0:
                idx = possible.pop(0)
                find_cost(cons_table, current_cost, idx, end)

# N: Date of resignation
N: int = int(input())

cons_table = list()

# T: Consultation period / P: Profit of consultation
for _ in range(N):
    T, P = map(int,input().split())

    cons_table.append((T, P))

max_cost = 0
result = 0

for i in range(N):
    # print(f'\n[Global Start Index: {i}]')
    max_cost = 0

    find_cost(cons_table, 0, i, N)

    if result < max_cost:
        result = max_cost

print(result)