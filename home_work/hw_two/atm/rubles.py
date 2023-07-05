from home_work.hw_two.atm.money import Money


class Rubles(Money):
    def __init__(self,value: float):
        super().__init__(value)
        self.sign = "Ꝑ"

    def set_value(self,value):
        self.value = value
    def get_value(self):
        return self.value

    def get_sign(self):
        return self.sign