import sys

from home_work.hw_two.atm import view



class Controller:
    def __init__(self,model,view):
        self.model = model
        self.view = view

    def start(self):
        while True:
            self.view.clear_console()
            self.view.main_menu()
            match self.view.input_data():
                case 1:
                    self.view.clear_console()
                    chooses = self.view.select_currency(self.model.get_card().get_money())
                    person_select = self.view.input_data() - 1
                    self.view.clear_console()
                    if person_select not in chooses:
                        self.view.error()
                        self.view.press_enter()
                        continue
                    self.model.deposit(person_select, self.view.input_ammount())
                    self.view.clear_console()
                    self.view.output_balance(self.model.get_card().get_money())
                case 2:
                    self.view.clear_console()
                    chooses = self.view.select_currency(self.model.get_card().get_money())
                    person_select = self.view.input_data() - 1
                    self.view.clear_console()
                    if person_select not in chooses:
                        self.view.error()
                        self.view.press_enter()
                        continue
                    self.model.withdraw(person_select, self.view.input_ammount())
                    self.view.clear_console()
                    self.view.output_balance(self.model.get_card().get_money())
                case 3:
                    sys.exit()