R, C = map(int, input().split())

information = list()
for _ in range(R):
    info = input()
    information.append(info)

visit_check = [[0]*C for _ in range(R)]     # ���� Ȯ�� �� �� / ���� Ȯ�� �������� ������ ����
sheep = 0
wolf = 0

for row in range(R):
    terr = list()   # '#'�� �ƴ� ���� ���� - BFS
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
            terr.append((row, col))     # �ش� row�� �湮 ������ ù ���� ����
            visit_check[row][col] = 1
            while len(terr) > 0:
                t = terr.pop(0)
                # �� / ���� Ȯ��
                if information[t[0]][t[1]] == 'v':
                    wo += 1
                elif information[t[0]][t[1]] == 'o':
                    sh += 1
                
                # ���� Ȯ�� �� �湮 ������ ���� ����
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
                    col = t[1]+1    # ���� �ֱٿ� Ȯ���� column���� ������Ʈ
            
            # �� / ������ �� ��
            if sh > wo:
                sheep += sh
            else:
                wolf += wo

print(sheep, wolf)