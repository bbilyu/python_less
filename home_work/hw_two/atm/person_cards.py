from home_work.hw_two.atm.bank_card import BankCard


class PersonCards:
    def __init__(self):
        self.cards = [BankCard]
    def get_number_cards(self):
        out = []
        for card in self.cards:
            out.append(card.get_number())
