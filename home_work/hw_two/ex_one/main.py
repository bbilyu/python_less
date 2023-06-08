"""Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата. """


class Model:
    def __init__(self):
        self.number = 0
        self.hex_string = ''

    def to_hex(self):
        """Переводит число в шестнадцатеричное представление"""
        hex_digits = "0123456789abcdef"
        result = ""
        num = self.number
        # Деление числа на 16 и запись остатков в обратном порядке
        while num > 0:
            rem = num % 16
            result = hex_digits[rem] + result
            num //= 16

        return result
    def check_hex(self):
        self.hex_string = hex(self.number)[2:]
        return self.hex_string


class View:
    def input_data(self):
        return int(input("Введите целое число: "))

    def output_main_result(self, hex_string):
        print(f"\n"
              f"Шестнадцатеричное представление: {hex_string}")

    def output_check_result(self, hex_string):
        print(f"\n"
              f"Шестнадцатеричное представление (с помощь hex): {hex_string}")


class Controller:
    def __init__(self,model,view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            try:
                self.model.number = self.view.input_data()
                hex_string = self.model.to_hex()
                self.view.output_main_result(hex_string)

                hex_string = self.model.check_hex()
                self.view.output_check_result(hex_string)
                break
            except ValueError:
                print("Ошибка! Введите целое число!")


if __name__ == '__main__':
    model = Model()
    view = View()
    controller = Controller(model,view)
    controller.run()