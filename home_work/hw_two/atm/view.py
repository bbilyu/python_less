class View:
    def main_menu(self):
        print("Главное меню:\n"
              "   1.Пополнить\n"
              "   2.Cнять\n"
              "   3.Выйти")
    def select_currency(self,currency:list):
        numers = []
        for num,curr in enumerate(currency):
            print(f"{num+1}.{curr.get_sign()}")
            numers.append(num)
        return numers
    def press_enter(self):
        input("Нажмите enter для продолжения....")
        print(500*"\n")
    def clear_console(self):
        print(500*"\n")
    def input_data(self):
        while True:
            try:
                return int(input("Выберите действие: "))
            except ValueError:
                print("Пожалуйста введите число!")
                continue
    def input_ammount(self):
        while True:
            try:
                amm = int(input("Введите cумму кратную 50 у.е: "))
                if not (amm % 50):
                    return amm
                else:
                    print("Ошибка!Сумма должна быть кратна 50 у.е!")
                    self.clear_console()
                    continue
            except ValueError:
                print("Ошибка!Пожалуйста введите число!")
                self.clear_console()

    def output_balance(self, currency):
        print("Баланс: \n")
        for curr in currency:
            print(f"{curr.get_value()} {curr.get_sign()}")
    def input_card_number(self):
        return int(input("Введите номер карты: "))
    def print_message(self,mess):
        print(mess)
    def error(self):
        print("Ошибка!")
    def value_error(self):
        print("Ошибка!Пожалуйста введите число!")

