R, C = map(int, input().split())

information = list()
for _ in range(R):
    info = input()
    information.append(info)

visit_check = [[0]*C for _ in range(R)]     # 영역 확인 및 양 / 늑대 확인 과정에서 재참조 방지
sheep = 0
wolf = 0

for row in range(R):
    terr = list()   # '#'이 아닌 영역 저장 - BFS
    col = 0
    while col < C:
        if visit_check[row][col] == 1:
            col += 1
        elif information[row][col] == '#':
            visit_check[row][col] = 1
            col += 1
        else:
            sh = 0
            wo = 0
            terr.append((row, col))     # 해당 row의 방문 가능한 첫 영역 저장
            visit_check[row][col] = 1
            while len(terr) > 0:
                t = terr.pop(0)
                # 양 / 늑대 확인
                if information[t[0]][t[1]] == 'v':
                    wo += 1
                elif information[t[0]][t[1]] == 'o':
                    sh += 1
                
                # 영역 확인 및 방문 가능한 영역 저장
                if t[0]-1 >= 0 and information[t[0]-1][t[1]] != '#' and visit_check[t[0]-1][t[1]] == 0:
                    terr.append((t[0]-1,t[1]))
                    visit_check[t[0]-1][t[1]] = 1
                if t[1]-1 >= 0 and information[t[0]][t[1]-1] != '#' and visit_check[t[0]][t[1]-1] == 0:
                    terr.append((t[0],t[1]-1))
                    visit_check[t[0]][t[1]-1] = 1
                if t[0]+1 < R and information[t[0]+1][t[1]] != '#' and visit_check[t[0]+1][t[1]] == 0:
                    terr.append((t[0]+1,t[1]))
                    visit_check[t[0]+1][t[1]] = 1
                if t[1]+1 < C and information[t[0]][t[1]+1] != '#' and visit_check[t[0]][t[1]+1] == 0:
                    terr.append((t[0],t[1]+1))
                    visit_check[t[0]][t[1]+1] = 1
                    col = t[1]+1    # 가장 최근에 확인한 column으로 업데이트
            
            # 양 / 늑대의 수 비교
            if sh > wo:
                sheep += sh
            else:
                wolf += wo

print(sheep, wolf)