from datetime import date

from home_work.hw_two.atm.atm import ATM
from home_work.hw_two.atm.bank_card import BankCard
from home_work.hw_two.atm.controller import Controller
from home_work.hw_two.atm.person import Person
from home_work.hw_two.atm.view import View

if __name__ == '__main__':
    person_one = Person("Герасимов","Кирилл","Михайлович")
    card_one = BankCard("Сбербанк",2022035203420532,date(1234,11,12),123,person_one)
    view = View()
    model = ATM(card_one)
    controller = Controller(model,view)
    controller.start()