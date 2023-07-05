from home_work.hw_two.atm.money import Money


class Dollars(Money):
    def __init__(self,value: float):
        super().__init__(value)
        self.sign = "$"

    def set_value(self, value: float):
        self.value = value

    def get_value(self):
        return self.value
    def get_sign(self):
        return self.sign