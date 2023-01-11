'''
# Recursion Function
def solution(maps):
    global answer, isVisit

    answer = 1000000
    isVisit = [[0]*len(maps[0]) for _ in range(len(maps))]
    find_shortest_path(maps, 0, 0, 0)
    if answer == 1000000:
        return -1
    else:
        return answer+1

def find_shortest_path(maps, row, col, count):
    global answer, isVisit

    # print(f'\nCurrent Position: ({row}, {col})')
    # print(f'Current Count: {count}')
    # print('Current Direction:')
    # for i in range(len(maps)):
    #     print(isVisit[i])
    
    if checking(maps, row, col, count):
        isVisit[row][col] = 1
        if count < answer and row == len(maps)-1 and col == len(maps[0])-1:
            answer = count
        find_shortest_path(maps, row+1, col, count+1)
        find_shortest_path(maps, row, col+1, count+1)
        find_shortest_path(maps, row-1, col, count+1)
        find_shortest_path(maps, row, col-1, count+1)
        isVisit[row][col] = 0

def checking(maps, row, col, count):
    global answer, isVisit

    if row != len(maps)-1 and col != len(maps[0])-1 and count >= answer:
        # print('Condition 1')
        return False

    if row < 0 or row >= len(maps) or col < 0 or col >= len(maps[0]) or maps[row][col] == 0 or isVisit[row][col] == 1:
        # print('Condition 2')
        return False
    
    return True
'''
def solution(maps):
    answer = -1
    queue = list()
    queue.append((0,0,1))

    while queue:
        row, col, distance = queue.pop(0)

        if row == len(maps)-1 and col == len(maps[0])-1:
            return distance
        
        if maps[row][col] == 0:
            continue

        maps[row][col] = 0
        if row+1 < len(maps):
            queue.append((row+1,col,distance+1))
        if col+1 < len(maps[0]):
            queue.append((row,col+1,distance+1))
        if row-1 >= 0:
            queue.append((row-1,col,distance+1))
        if col-1 >= 0:
            queue.append((row,col-1,distance+1))
     
    return answer

# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
# maps = [[1,1,1,1,1],[1,0,1,0,0],[1,1,1,0,1],[0,0,1,1,1],[1,1,1,0,1]]
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1]]

print(solution(maps))