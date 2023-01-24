R, C = map(int,input().split())

board = list()
for _ in range(R):
    board.append(input())

maxLength = 0

queue = list()
queue.append((0,0,board[0][0]))
while queue:
    row, col, record = queue.pop(0)

    if maxLength < len(record):
        maxLength = len(record)

    if row + 1 < R and board[row+1][col] not in record:
        queue.append((row+1,col,record + board[row+1][col]))
    if col + 1 < C and board[row][col+1] not in record:
        queue.append((row,col+1,record + board[row][col+1]))
    if row - 1 >= 0 and board[row-1][col] not in record:
        queue.append((row-1,col,record + board[row-1][col]))
    if col - 1 >= 0 and board[row][col-1] not in record:
        queue.append((row,col-1,record + board[row][col-1]))

print(maxLength)

# 시간 초과...