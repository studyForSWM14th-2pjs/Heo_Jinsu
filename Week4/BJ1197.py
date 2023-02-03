import sys

# V: 정점의 수 | E: 간선의 수
V, E = map(int,input().split())

total_cost = 0

''' # Prim Algorithm    -> 메모리 초과...
weights = [[sys.maxsize]*(V+1) for _ in range(V+1)]

for _ in range(E):
    A, B, C = map(int,input().split())
    weights[A][B] = C
    weights[B][A] = C

isVisit = [False]*(V+1)
nearest = [1]*(V+1)
distance = weights[1]

for v in range(V-1):
    mini = sys.maxsize
    for i in range(2,V+1):
        if not isVisit[i] and distance[i] < mini:
            mini = distance[i]
            vnear = i
    total_cost += distance[vnear]
    isVisit[vnear] = True
    for i in range(2,V+1):
        if not isVisit[i] and weights[i][vnear] < distance[i]:
            distance[i] = weights[i][vnear]
            nearest[i] = vnear
'''
# Kruskal Algorithm -> 시간 초과...
def find(i):
    while U[i] != i:
        i = U[i]
    return i

def merge(a,b):
    if (a < b):
        U[b] = a
    else:
        U[a] = b

edges = list()
U = [-1]*(V+1)

for _ in range(E):
    A, B, C = map(int,input().split())
    edges.append((A,B,C))

edges = sorted(edges, key=lambda x: x[2])
for i in range(1,V+1):
    U[i] = i

while edges:
    a, b, c = edges.pop(0)
    p = find(a)
    q = find(b)
    if p != q:
        merge(p, q)
        total_cost += c

print(total_cost)