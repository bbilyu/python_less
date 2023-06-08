""" Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем
и знаменателем. Программа должна
возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions. """


from fractions import Fraction


def gcd_fractions(numerator, denominator):
    while denominator != 0:
        numerator, denominator = denominator, numerator % denominator

    return numerator


class Model:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def sum_of_fractions(self):
        if self.b == self.d:
            numerator = self.a + self.c
            denominator = self.b
            gcd = gcd_fractions(numerator, denominator)
            return f"{int(numerator / gcd)}/{int(denominator / gcd)}"
        else:
            numerator = (self.a * self.d) + (self.c * self.b)
            denominator = self.b * self.d
            gcd = gcd_fractions(numerator, denominator)
            return f"{int(numerator / gcd)}/{int(denominator / gcd)}"

    def multiply_of_fractions(self):
        numerator = self.a * self.c
        denominator = self.b * self.d
        gcd = gcd_fractions(numerator, denominator)
        return f"{int(numerator / gcd)}/{int(denominator / gcd)}"

    def check_sum_of_fractions(self):
        result = Fraction(self.a, self.b) + Fraction(self.c, self.d)
        return result

    def check_multiply_of_fractions(self):
        result = Fraction(self.a, self.b) * Fraction(self.c, self.d)
        return result


class View:
    def input_data(self):
        return input("Введите две дроби через '/': ")

    def output_main_result(self, result_add, result_multiply):
        print(f"\n"
              f"Основной расчет:")
        print(f"Сумма дробей: {result_add}")
        print(f"Произведение дробей: {result_multiply}")

    def output_check_result(self, result_add, result_multiply):
        print(f"\n"
              f"Проверка с помощью Fraction:")
        print(f"Сумма дробей: {result_add}")
        print(f"Произведение дробей: {result_multiply}")


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            try:
                data = self.view.input_data().split('/')
                a = int(data[0])
                b = int(data[1])
                data = self.view.input_data().split('/')
                c = int(data[0])
                d = int(data[1])

                self.model = Model(a, b, c, d)
                result_check_sum = self.model.check_sum_of_fractions()
                result_check_multiply = self.model.check_multiply_of_fractions()
                result_sum = self.model.sum_of_fractions()
                result_multiply = self.model.multiply_of_fractions()

                self.view.output_main_result(result_sum, result_multiply)
                self.view.output_check_result(result_check_sum, result_check_multiply)
                break
            except ValueError:
                print("Пожалуйста введите число дробью как в примере!")


if __name__ == '__main__':
    model = Model(0, 0, 0, 0)
    view = View()
    controller = Controller(model, view)
    controller.run()
