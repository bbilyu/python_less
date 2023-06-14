""" Напишите функцию для транспонирования матрицы"""


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transposed_matrix = transpose(matrix)
    print(transposed_matrix)
