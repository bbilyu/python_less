"""Задание №3
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения
возраста на год, full_name для вывода полного ФИО и т.п. на
ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого
изменения, но есть возможность получить текущий возраст"""


class Human:
    def __init__(self, name, surname, patronymic, birthday = None, weight=None, heigh=None, gender=None):
        self.name = str(name).title()
        self.surname = str(surname).title()
        self.patronymic = str(patronymic).title()
        self._birthday = int(birthday) if birthday else None
        self.weight = int(weight) if weight else None
        self.heigh = int(heigh) if heigh else None
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

    def get_birthday(self):
        return self._birthday

    def birthday(self):
        if self._birthday:
            self._birthday += 1
        else:
            self._birthday = 1

    def get_full_name(self):
        return f"ФИО: {self.patronymic} {self.name} {self.surname}"


if __name__ == '__main__':
    hum_one = Human(name="ВАСИЛИЙ", surname="Петрович", patronymic="Моргунов", weight="80", heigh="120", gender="male",
                    birthday="23")
    print(hum_one.get_full_name())
    print(hum_one.get_birthday())
    hum_one.birthday()
    print(hum_one.get_birthday())
