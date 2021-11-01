def is_valid_square(maze, row, column, n):
    if 0 <= row < n and 0 <= column < n and maze[row][column] == 1:
        return True
    else:
        return False


def solve_maze(maze, row, column, correct_path, n):
    if row == n - 1 and column == n - 1 and maze[row][column] == 1:
        correct_path[row][column] = 1
        return True
    if is_valid_square(maze, row, column, n):
        correct_path[row][column] = 1

        if solve_maze(maze,row+1,column,correct_path,n):
            return True
        if solve_maze(maze,row,column+1,correct_path,n):
            return True
        maze[row][column] = 0
        return False
    return False
