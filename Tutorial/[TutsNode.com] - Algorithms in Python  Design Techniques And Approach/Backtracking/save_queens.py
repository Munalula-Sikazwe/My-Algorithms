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