"""
Задание №2
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра
"""


class Archive:
    """Класс Archive представляет архив игроков и предоставляет функциональность для создания и отображения
    информации об игроках. """
    _instance = None
    _archive = []

    def __new__(cls, name: str, age: int):
        """Создает новый объект класса Archive с указанным именем и возрастом игрока. Возвращает созданный объект.
        Если уже существует объект класса Archive, он добавляется в архив. Метод использует механизм одиночки,
        поэтому всегда возвращает один и тот же экземпляр класса Archive. """
        instance = super().__new__(cls)
        if cls._instance:
            cls._archive.append(cls._instance)
        cls._instance = instance
        instance.archive = cls._archive.copy()
        return cls._instance

    def __init__(self, name: str, age: int):
        """Инициализирует объект класса Archive с указанным именем и возрастом игрока."""
        self.name = name
        self.age = age

    def __str__(self):
        """Возвращает строковое представление игрока, включающее имя, возраст и список предыдущих игроков из архива."""
        return f'Игрок по имени {self.name} ({self.age} лет). До него были созданы игроки: {[pl.name for pl in self.archive]} '

    def __repr__(self):
        """ Возвращает строковое представление игрока, содержащее только имя и возраст."""
        return f"{self.name} {self.age}"


if __name__ == '__main__':
    help(Archive)
    player_one = Archive('STONE', 39)
    print(player_one)
    player_one = Archive('Karina', 19)
    print(player_one)
