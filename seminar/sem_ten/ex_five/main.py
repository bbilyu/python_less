"""
Задание №5
Создайте три (или более) отдельных классов животных.
Например рыбы, птицы и т.п.
У каждого класса должны быть как общие свойства,
например имя, так и специфичные для класса.
Для каждого класса создайте метод, выводящий
информацию специфичную для данного класса
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        pass


class Fish(Animal):
    def __init__(self, name, water_type):
        super().__init__(name)
        self.water_type = water_type

    def get_info(self):
        print(f"Fish Name: {self.name}")
        print(f"Water Type: {self.water_type}")


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def get_info(self):
        print(f"Bird Name: {self.name}")
        print(f"Wingspan: {self.wingspan} cm")


class Mammal(Animal):
    def __init__(self, name, habitat):
        super().__init__(name)
        self.habitat = habitat

    def get_info(self):
        print(f"Mammal Name: {self.name}")
        print(f"Habitat: {self.habitat}")


if __name__ == '__main__':
    fish = Fish("Nemo", "Saltwater")
    bird = Bird("Eagle", 200)
    mammal = Mammal("Tiger", "Jungle")

    fish.get_info()
    print("--------")
    bird.get_info()
    print("--------")
    mammal.get_info()
    print("--------")
