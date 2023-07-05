"""Доработаем задачи 5-6. Создайте класс-фабрику.
○ Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
○ Внутри класса создайте экземпляр на основе переданного типа и
верните его из класса-фабрики."""

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args, **kwargs):
        if animal_type == "Fish":
            return Fish(*args, **kwargs)
        elif animal_type == "Bird":
            return Bird(*args, **kwargs)
        elif animal_type == "Mammal":
            return Mammal(*args, **kwargs)
        else:
            raise ValueError(f"Invalid animal type: {animal_type}")


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
    factory = AnimalFactory()
    try:
        fish = factory.create_animal("Fish", "Nemo", "Saltwater")
        bird = factory.create_animal("Bird", "Eagle", 200)
        mammal = factory.create_animal("Mammal", "Tiger", "Jungle")
        spider = factory.create_animal("Spider", "Black widow", "poisonous")
    except ValueError as e:
        print(e)
    print("--------")
    fish.get_info()
    print("--------")
    bird.get_info()
    print("--------")
    mammal.get_info()