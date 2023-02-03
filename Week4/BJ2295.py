N = int(input())

U = list()
for _ in range(N):
    U.append(int(input()))
U.sort()

def find_value():
    global N, U
    for x in range(N-2,-1,-1):
        for y in range(N-2,-1,-1):
            if U[x]+U[y] > U[N-1]:
                continue
            for z in range(N-2,-1,-1):
                if U[x]+U[y]+U[z] > U[N-1]:
                    continue
                if (U[x]+U[y]+U[z]) in U:
                    print(U[x]+U[y]+U[z])
                    return
find_value()
# Æ²¸²...