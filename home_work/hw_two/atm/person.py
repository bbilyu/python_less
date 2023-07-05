
from home_work.hw_two.atm.human import Human


class Person(Human):
    def __init__(self,surname,name,patronymic):
        super().__init__(name, surname, patronymic)
        self._bank_cards = []
        self._place_of_work = None
        self._place_of_study = None
        self._registration = None
        self._phone_number = None

    def set_bank_cards(self, bank_cards: []):
        self._bank_cards = bank_cards

    def set_place_of_work(self, place_of_work: str):
        self._place_of_work = place_of_work

    def set_place_of_study(self, place_of_study: str):
        self._place_of_study = place_of_study

    def set_registration(self, registration: str):
        self._registration = registration

    def set_phone_number(self, phone_number: int):
        self._phone_number = phone_number

    def get_cards(self):
        return self._bank_cards

    def get_place_of_work(self):
        return self._place_of_work

    def get_place_of_study(self):
        return self._place_of_study

    def get_registration(self):
        return self._registration

    def get_phone_number(self):
        return self._phone_number

    def append_card(self, card):
        self._bank_cards.append(card)

    def remove_card(self, card):
        self._bank_cards.remove(card)
