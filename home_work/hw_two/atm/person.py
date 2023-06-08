
from home_work.hw_two.atm.human import Human


class Person(Human):
    def __init__(self,surname,name,patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.bank_cards = []
        self.place_of_work = None
        self.place_of_study = None
        self.registration = None
        self.phone_number = None

    def set_bank_cards(self, bank_cards: []):
        self.bank_cards = bank_cards

    def set_place_of_work(self, place_of_work: str):
        self.place_of_work = place_of_work

    def set_place_of_study(self, place_of_study: str):
        self.place_of_study = place_of_study

    def set_registration(self, registration: str):
        self.registration = registration

    def set_phone_number(self, phone_number: int):
        self.phone_number = phone_number

    def get_cards(self):
        return self.bank_cards

    def get_place_of_work(self):
        return self.place_of_work

    def get_place_of_study(self):
        return self.place_of_study

    def get_registration(self):
        return self.registration

    def get_phone_number(self):
        return self.phone_number

    def append_card(self, card):
        self.bank_cards.append(card)

    def remove_card(self, card):
        self.bank_cards.remove(card)
