from home_work.hw_two.atm.bank_card import BankCard


class ATM:
    def __init__(self,card: BankCard):
        self.card = card
        self.serial_number = None
        self.company_name = None
        self.capacity = None
        self.money = []
        self.cards = []

    def set_serial_number(self,serial_number: int):
        self.serial_number = serial_number
    def set_company_name(self,company_name: str):
        self.company_name = company_name
    def set_capacity(self,capacity: str):
        self.capacity = capacity
    def set_money(self,money: []):
        self.money = money
    def set_cards(self,cards: []):
        self.cards = cards

    def get_serial_number(self):
        return self.serial_number
    def get_company_name(self):
        return self.company_name
    def get_capacity(self):
        return self.capacity
    def get_money(self):
        return self.money
    def get_card(self):
        return self.card

    def deposit(self,currency,amount:int):
        balance = self.card.get_money()[currency].get_value()
        self.card.get_money()[currency].set_value(balance+amount)
        self.card.operations_count += 1
        if self.card.operations_count % 3 == 0:
            balance = self.card.get_money()[currency].get_value()
            self.card.get_money()[currency].set_value(balance*1.03)

    def withdraw(self,currency,amount:int):
        balance = self.card.get_money()[currency].get_value()
        if amount > balance:
            return False
        if balance >= 5000000:
            tax = balance * 0.1
            self.card.get_money()[currency].set_value(balance - tax)
        fee = amount * 0.015
        if fee < 30:
            fee = 30
        elif fee > 600:
            fee = 600
        amount += fee
        balance = self.card.get_money()[currency].get_value()
        self.card.get_money()[currency].set_value(balance - amount)
        balance = self.card.get_money()[currency].get_value()
        self.card.operations_count += 1
        if self.card.operations_count % 3 == 0:
            self.card.get_money()[currency].set_value(balance * 1.03)

