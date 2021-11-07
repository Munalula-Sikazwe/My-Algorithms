my_dict = {'RAY', 'APPLE', 'FAKE', 'BOOKS'}

row_index = 4
column_index = 4


def is_valid_cell(row, column, visited):
    if 0 <= row < row_index and 0 <= column < column_index and visited[row, column] == 0:
        return True
    return False


def find_words(boggle, visited, row_index_param, column_index_param, word):
    word = ''.join([word, boggle[row_index_param][column_index_param]])
    visited[row_index_param][column_index_param] = 1

    if word in my_dict:
        print(word)
    for row in range(row_index_param - 1, row_index_param + 2):
        for column in range(column_index_param - 1, column_index_param + 2):
            if is_valid_cell(row, column, visited):
                find_words(boggle, visited, row, column, word)

    visited[row_index_param][column_index_param] = 0


boogle = [['T', 'Y', 'R', 'S'],
          ['N', 'U', 'A', 'K'],
          ['Z', 'F', 'E', 'O'],
          ['A', 'C', 'B', 'O']]

visited = [[0 for _ in range(len(boogle))] for _ in range(len(boogle))]

for i in range(row_index):
    for j in range(column_index):
        find_words(boogle, visited, row_index, column_index, '')
