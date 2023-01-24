import sys

# V: 정점의 수 | E: 간선의 수
V, E = map(int,input().split())

weights = [[sys.maxsize]*(V+1) for _ in range(V+1)]

for _ in range(E):
    A, B, C = map(int,input().split())
    weights[A][B] = C
    weights[B][A] = C

isVisit = [False]*(V+1)
nearest = [1]*(V+1)
distance = weights[1]
total_mini = 0

for v in range(V-1):
    mini = sys.maxsize
    for i in range(2,V+1):
        if not isVisit[i] and distance[i] < mini:
            mini = distance[i]
            vnear = i
    total_mini += distance[vnear]
    isVisit[vnear] = True
    for i in range(2,V+1):
        if not isVisit[i] and weights[i][vnear] < distance[i]:
            distance[i] = weights[i][vnear]
            nearest[i] = vnear

print(total_mini)

# Prim Algorithm -> 메모리 초과...
# Kruskal Algorithm -> 시도