"""Задание №2
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class NegativeSideError(Exception):
    def __str__(self):
        return f"Ошибка! Значение стороны должно быть больше нуля!"


class Rectangle:
    def __init__(self, length, width):
        if length < 0 or width < 0:
            raise NegativeSideError
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length + self.width) * 2

    def square(self):
        return self.length * self.width


if __name__ == '__main__':
    try:
        rec_one = Rectangle(length=-10, width=20)
        print(rec_one.perimeter())
        print(rec_one.square())
    except NegativeSideError as e:
        print(e)

