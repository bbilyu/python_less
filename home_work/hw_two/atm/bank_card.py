from datetime import date

from home_work.hw_two.atm.dollars import Dollars
from home_work.hw_two.atm.money import Money
from home_work.hw_two.atm.person import Person
from home_work.hw_two.atm.rubles import Rubles


class BankCard:
    def __init__(self,organization: str ,number: int, expiration_date: date, cvc: int, cardholder: Person):
        self.organization = organization
        self.operations_count = 0
        self.number = number
        self.expiration_date = expiration_date
        self.cvc = cvc
        self.cardholder = cardholder
        self.money = [Rubles(0),Dollars(0)]

    def set_organization(self,organization: str):
        self.organization = organization
    def set_number(self,number: int):
        self.number = number
    def set_expiration_date(self,expiration_date: date):
        self.expiration_date = expiration_date
    def set_cvc(self,cvc):
        self.cvc = cvc
    def set_cardholder(self,cardholder: Person):
        self.cardholder = cardholder
    def set_money(self,money: list):
        self.money = money

    def get_organization(self):
        return self.organization
    def get_number(self):
        return self.number
    def get_expiration_date(self):
        return self.expiration_date
    def get_cvc(self):
        return self.cvc
    def get_cardholder(self):
        return self.cardholder
    def get_cardholder_name(self):
        return self.cardholder.get_name()
    def get_cardholder_surname(self):
        return self.cardholder.get_surname()
    def get_money(self):
        return self.money

    def append_currency(self,currency: Money):
        self.money.append(currency)
