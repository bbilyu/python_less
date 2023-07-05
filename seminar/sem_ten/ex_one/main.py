"""Задание №1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании
экземпляра.
У класса должно быть два метода, возвращающие длину
окружности и её площадь."""
from math import pi


class Circle:
    def __init__(self, radius=None):
        self.radius = radius

    def circumference_length(self):
        return 2 * pi * self.radius

    def square(self):
        return pi * self.radius**2

if __name__ == '__main__':
    circ_one = Circle(radius=80)
    print(circ_one.circumference_length())
    print(circ_one.square())