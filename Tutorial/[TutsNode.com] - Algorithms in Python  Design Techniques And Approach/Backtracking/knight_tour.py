global path_x, path_y, n
n = 8
path_x = [2, 1, -1, -2, -2, -1, 1, 2]
path_y = [1, 2, 2, 1, -1, -2, -2, -1]


def valid_move(board, row, column, n):
    if 0 <= row < n and 0 <= column < n and board[row][column] == -1:
        return True
    return False


def knight_tour(board, step, row=0, column=0, n=8):
    if step == n ** 2:
        return True

    for index in range(n):
        row_new = row + path_x[index]
        column_new = column + path_y[index]
        if valid_move(board, row_new, column_new, n):
            board[row_new][column_new] = step
            if knight_tour(board, row, column, step + 1, n):
                return True
            board[row_new][column_new] = -1
    return False


board = [[-1 for _ in range(n)] for _ in range(n)]
board[0][0] = 0
step = 1
if knight_tour(board, step):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
    print()
else:
    print("Solution for this position does not exist.")
