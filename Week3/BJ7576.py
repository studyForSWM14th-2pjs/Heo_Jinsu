# M (Column), N (Row) : Shape of box
M, N = map(int,input().split())

# 토마토 저장 정보 - 0:익지 않은 토마토 | 1: 익은 토마토 | -1: 토마토 없음
tomatos = list()
for i in range(N):
    tomatos.append(list(map(int,input().split())))

days = 0

# 푸는 중...