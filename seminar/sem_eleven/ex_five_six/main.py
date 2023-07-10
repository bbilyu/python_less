class Square:
    """Класс Square представляет квадрат и предоставляет основные операции с ним."""
    def __init__(self, a, b=None):
        self.a = a
        self.b = b if b else a

    def area(self):
        """Возвращает площадь квадрата, вычисляемую как произведение сторон a и b."""
        return self.a * self.b

    def perimeter(self):
        """Возвращает периметр квадрата, вычисляемый как удвоенная сумма сторон a и b."""
        return 2 * (self.a + self.b)

    def __add__(self, other):
        """Возвращает новый объект класса Square, являющийся результатом сложения сторон квадратов self и other."""
        new_a = self.a + other.a
        new_b = self.b + other.b
        return Square(new_a, new_b)

    def __sub__(self, other):
        """Возвращает новый объект класса Square, являющийся результатом вычитания сторон квадратов other из сторон
        квадрата self. Если результатом вычитания являются отрицательные значения, вызывается исключение ValueError. """
        if self.a - other.a < 0 or self.b - other.b < 0:
            raise ValueError
        new_a = self.a - other.a
        new_b = self.b - other.b
        return Square(new_a, new_b)

    def __eq__(self, other):
        """Проверяет, является ли площадь квадрата self равной площади квадрата other и возвращает булево значение
        True или False соответственно. """
        return self.area() == other.area()

    def __le__(self, other):
        """Проверяет, является ли площадь квадрата self меньшей или равной площади квадрата other и возвращает булево
        значение True или False соответственно. """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Проверяет, является ли площадь квадрата self большей чем площадь квадрата other и возвращает булево
        значение True или False соответственно. """
        return self.area() > other.area()


if __name__ == '__main__':
    help(Square)
    square_one = Square(10, 6)
    square_two = Square(2, 1)
    print(square_one > square_two)
    print(square_one < square_two)
    print(square_one == square_two)
    print(square_one != square_two)
    print(square_one >= square_two)
    print(square_one <= square_two)
    # square_three = square_one + square_two
    # square_three = square_two - square_one
