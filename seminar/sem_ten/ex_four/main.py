"""Задание №4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр id на семь"""
from random import randint

from seminar.sem_ten.ex_three.main import Human


class Stuff(Human):
    def __init__(self,name,surname,patronymic):
        self.id = randint(100000,999999)
        self._place_of_work = None
        self._place_of_study = None
        self._registration = None
        self._phone_number = None
        super().__init__(name=name, surname=surname, patronymic=patronymic)

    @property
    def acess_level(self):
        return sum(list(map(int,str(self.id)))) % 7

    def set_place_of_work(self, place_of_work: str):
        self.place_of_work = place_of_work

    def set_place_of_study(self, place_of_study: str):
        self.place_of_study = place_of_study

    def set_registration(self, registration: str):
        self.registration = registration

    def set_phone_number(self, phone_number: int):
        self.phone_number = phone_number

    def get_place_of_work(self):
        return self._place_of_work

    def get_place_of_study(self):
        return self._place_of_study

    def get_registration(self):
        return self._registration

    def get_phone_number(self):
        return self._phone_number

if __name__ == '__main__':
    stuff_one = Stuff(name="ВАСИЛИЙ", surname="Петрович", patronymic="Моргунов")
    print(f"id = {stuff_one.id}")
    print(f"acess_level = {stuff_one.acess_level}")
