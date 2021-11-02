def is_safe_square(board, row, col, size):
    """
    check if a queen exists in a the previous column  which is  horizontally
    aligned with the current square. In short checking for a queen on a given rank.

    """
    for rank in range(col):
        if board[row][rank] == 1:
            return False

    """
    check if a queen is aligned in the upper left diagonal with the current square.
    """

    for rank, file in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[rank][file] == 1:
            return False

    """
    check if a queen is aligned in the lower left diagonal with the current square.
    """

    for rank, file in zip(range(row, size), range(col, -1, -1)):
        if board[rank][file] == 1:
            return False
    return True


def save_queens(board, col, size):
    if col >= size:
        return True

    for i in range(size):
        if is_safe_square(board, i, col, size):
            board[i][col] = 1

            if save_queens(board, col + 1, size):
                return True
            ## perform backtracking

            board[i][col] = 0


board = [[0 for _ in range(5)] for _ in range(5)]
size = len(board)

if save_queens(board,0,size):
    for i in board:
        for j in i:
            print(j, end=' ')
        print()
