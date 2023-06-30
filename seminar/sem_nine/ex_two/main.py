"""Задание №2
Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов"""

from typing import Callable
from random import randint


def main(func: Callable):

    def wrapper(num_range, attempts):
        num_range = num_range if 1 < num_range < 100 else randint(1, 100)
        attempts = attempts if 1 < num_range < 10 else randint(1, 10)
        result = func(num_range, attempts)
        return result

    return wrapper


@main
def game(num_range, attempts):
    
    num_sc = randint(1, num_range)
    while attempts:
        print(f'Осталось {attempts} попыток.', end=" ")
        attempts -= 1
        num = int(input("Введите число: "))
        if num == num_sc:
            print("Угадал,поздравляю!")
            break
        else:
            advice = ['больше', 'меньше']
            print(f"Не угадал,введите число {advice[num > num_sc]}")
    else:
        print(f"Ты проиграл! Правильное число {num_sc}")


if __name__ == '__main__':
    game(101, 11)
