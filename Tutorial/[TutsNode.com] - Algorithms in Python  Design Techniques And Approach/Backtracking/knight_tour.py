board_size = 8


def valid_move(board, row, column, n):
    if 0 <= row < n and 0 <= column < n and board[row][column] == -1:
        return True
    return False


def knight_tour(board, step, board_size, row=0, column=0, n=8):
    path_x = [2, 1, -1, -2, -2, -1, 1, 2]
    path_y = [1, 2, 2, 1, -1, -2, -2, -1]
    if step == board_size ** 2:
        print("reached edge case.")
        return True

    for index in range(n):
        row_new = row + path_x[index]
        column_new = column + path_y[index]
        if valid_move(board, row_new, column_new, board_size):
            board[row_new][column_new] = step
            if knight_tour(board, step + 1, board_size, row=row_new, column=column_new):
                return True

            board[row_new][column_new] = -1

    return False


board = [[-1 for _ in range(board_size)] for _ in range(board_size)]
board[0][0] = 0
step = 1
if knight_tour(board, step, board_size, row=0, column=0):
    for i in range(board_size):
        for j in range(board_size):
            print(board[i][j], end=' ')
        print()
else:
    for i in range(board_size):
        for j in range(board_size):
            print(board[i][j], end=' ')
        print()
    print("Solution for this position does not exist.")
