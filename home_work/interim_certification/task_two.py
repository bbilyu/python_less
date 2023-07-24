import doctest
import logging

logging.basicConfig(filename='matrix.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class Matrix:
    """Класс Matrix представляет матрицу и предоставляет методы для работы с матрицами."""

    def __init__(self, elements):
        """Инициализирует объект класса Matrix с указанными элементами матрицы."""
        self.elements = elements

    def __str__(self):
        """Возвращает строковое представление матрицы, где каждая строка матрицы разделена новой строкой, а элементы
        в строке разделены табуляцией. """
        return '\n'.join(['\t'.join(map(str, row)) for row in self.elements])

    def __eq__(self, other):
        """Сравнивает текущую матрицу с другой матрицей other и возвращает булево значение True, если матрицы равны,
        и False в противном случае. """
        logger.info(f' РАВЕНСТВО:  {self.elements} = {other.elements} ')
        return self.elements == other.elements

    def __add__(self, other):
        """Складывает текущую матрицу с другой матрицей other и возвращает новый объект класса Matrix, содержащий
        результат сложения матриц. Матрицы должны быть одинакового размера для выполнения операции сложения. В
        противном случае вызывается исключение ValueError. """
        if len(self.elements) != len(other.elements) or len(self.elements[0]) != len(other.elements[0]):
            logger.error(
                f'Не возможно выполнить сложение матриц, размерности матриц несовместимы:  [{len(self.elements)}][{len(self.elements[0])}] !=  [{len(other.elements)}][{len(other.elements[0])}] ')
            raise ValueError("Матрицы должны быть одинакового размера для сложения.")
        result = []
        for i in range(len(self.elements)):
            row = []
            for j in range(len(self.elements[0])):
                row.append(self.elements[i][j] + other.elements[i][j])
            result.append(row)
        out_marix = Matrix(result)
        logger.info(f' СЛОЖЕНИЕ:  {self.elements} + {other.elements} = {out_marix}  ')
        return out_marix

    def __mul__(self, other):
        """Умножает текущую матрицу на другую матрицу other и возвращает новый объект класса Matrix, содержащий
        результат умножения матриц. Количество столбцов в первой матрице должно быть равно количеству строк во второй
        матрице для выполнения операции умножения. В противном случае вызывается исключение ValueError. """
        if len(self.elements[0]) != len(other.elements):
            logger.error(
                f'Не возможно выполнить умножение матриц, размерности матриц несовместимы: [{len(self.elements)}][{len(self.elements[0])}] !=  [{len(other.elements)}][{len(other.elements[0])}]')
            raise ValueError(
                "Количество столбцов в первой матрице должно быть равно количеству строк во второй матрице для "
                "умножения.")
        result = []
        for i in range(len(self.elements)):
            row = []
            for j in range(len(other.elements[0])):
                element = 0
                for k in range(len(other.elements)):
                    element += self.elements[i][k] * other.elements[k][j]
                row.append(element)
            result.append(row)
        out_marix = Matrix(result)
        logger.info(f' УМНОЖЕНИЕ:  {self.elements} * {other.elements} = {out_marix}  ')
        return out_marix


# def test_Matrix():
#     """
#     >>> matrix1 = Matrix([[1, 2], [3, 4]])
#     >>> print(matrix1)
#     '1\t2\n3\t4'
#
#     >>> matrix1 = Matrix([[1, 2], [3, 4]])
#     >>> matrix2 = Matrix([[1, 2], [3, 4]])
#     >>> print(matrix1==matrix2)
#     True
#
#     >>> matrix3 = Matrix([[1, 2], [3, 4]])
#     >>> matrix4 = Matrix([[5, 6], [7, 8]])
#     >>> print(matrix3+matrix4)
#     '6\t8\n10\t12'
#
#     >>> matrix5 = Matrix([[1, 2], [3, 4], [5, 6]])
#     >>> matrix6 = Matrix([[1, 2, 3], [4, 5, 6]])
#     >>> print(matrix5 * matrix6)
#     '9\t12\t15\n19\t26\t33\n29\t40\t51'
#     """

if __name__ == '__main__':
    # Создание матрицы
    matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
    matrix2 = Matrix([[7, 8, 9], [10, 11, 12]])

    # Вывод на печать
    print(matrix1)
    print(matrix2)

    # Сравнение
    print(matrix1 == matrix2)

    # Сложение
    matrix_sum = matrix1 + matrix2
    print(matrix_sum)

    # Умножение
    matrix_product = matrix1 * matrix2
    print(matrix_product)
