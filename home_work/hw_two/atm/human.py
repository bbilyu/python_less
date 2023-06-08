class Human:
    def __init__(self, name, surname, patronymic,weight,heigh,gender):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.weight = weight
        self.heigh = heigh
        self.gender = gender

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def set_patronymic(self, patronymic):
        self.patronymic = patronymic

    def set_weight(self, weight):
        self.weight = weight

    def set_heigh(self, heigh):
        self.heigh = heigh

    def set_gender(self, gender):
        self.gender = gender

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_patronymic(self):
        return self.patronymic

    def get_weight(self):
        return self.weight

    def get_heigh(self):
        return self.heigh

    def get_gender(self):
        return self.gender
