"""
2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны
предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в
одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно
сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""


class ZeroSideError(Exception):
    def __str__(self):
        return f"Ошибка! Значение стороны должно быть равно нулю!"


class NegativeSideError(Exception):
    def __str__(self):
        return f"Ошибка! Значение стороны должно быть больше нуля!"


class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if not (side_a or side_b or side_c):
            raise ZeroSideError
        if side_a < 0 or side_b < 0 or side_c < 0:
            raise NegativeSideError
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_sides(self):
        return [self.side_a, self.side_b, self.side_c]

    def check_triangle(self):
        if self.side_a < (self.side_b + self.side_c) and self.side_b < (self.side_a + self.side_c) and self.side_c < (
                self.side_a + self.side_b):
            if self.side_a == self.side_b == self.side_c:
                return "Треугольник равносторонний"
            elif (self.side_a == self.side_b) or (self.side_b == self.side_c) or (self.side_c == self.side_a):
                return "Треугольник равнобедренный"
            else:
                return "Треугольник разносторонний"

        else:
            return "Треугольник не существует"

    def __str__(self):
        return f"A = {self.side_a} \nB = {self.side_b}\nC = {self.side_c}"


if __name__ == '__main__':
    while True:
        try:
            side_a = int(input("Введите значние стороны a: "))
            side_b = int(input("Введите значние стороны b: "))
            side_c = int(input("Введите значние стороны c: "))
            trig_one = Triangle(side_a, side_b, side_c)
            print(trig_one.check_triangle())
            print(trig_one.get_sides())
            print(trig_one)
            break
        except ValueError:
            print("Пожалуйста введите целое число!")
            continue
        except ZeroSideError as e:
            print(e)
            continue
        except NegativeSideError as e:
            print(e)
            continue
