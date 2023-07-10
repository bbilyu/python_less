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
        return self.elements == other.elements

    def __add__(self, other):
        """Складывает текущую матрицу с другой матрицей other и возвращает новый объект класса Matrix, содержащий
        результат сложения матриц. Матрицы должны быть одинакового размера для выполнения операции сложения. В
        противном случае вызывается исключение ValueError. """
        if len(self.elements) != len(other.elements) or len(self.elements[0]) != len(other.elements[0]):
            raise ValueError("Матрицы должны быть одинакового размера для сложения.")

        result = []
        for i in range(len(self.elements)):
            row = []
            for j in range(len(self.elements[0])):
                row.append(self.elements[i][j] + other.elements[i][j])
            result.append(row)

        return Matrix(result)

    def __mul__(self, other):
        """Умножает текущую матрицу на другую матрицу other и возвращает новый объект класса Matrix, содержащий
        результат умножения матриц. Количество столбцов в первой матрице должно быть равно количеству строк во второй
        матрице для выполнения операции умножения. В противном случае вызывается исключение ValueError. """
        if len(self.elements[0]) != len(other.elements):
            raise ValueError("Количество столбцов в первой матрице должно быть равно количеству строк во второй "
                             "матрице для умножения.")

        result = []
        for i in range(len(self.elements)):
            row = []
            for j in range(len(other.elements[0])):
                element = 0
                for k in range(len(other.elements)):
                    element += self.elements[i][k] * other.elements[k][j]
                row.append(element)
            result.append(row)

        return Matrix(result)


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
