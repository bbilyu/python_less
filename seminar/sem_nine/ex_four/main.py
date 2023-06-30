"""Задание №4
Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.
"""
import random
from typing import Callable


def count(num: int = 1):
    def deco(func: Callable):
        rand_num = random.randint(0, 10)

        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                if result == rand_num:
                    print("Угадал,поздравляю!")
                    break
                else:
                    print("Не угадал,введите число " + ("меньше" if result > rand_num else "больше"))
            return result

        return wrapper

    return deco


@count(10)
def get_number() -> [int, int]:
    while True:
        try:
            return int(input("Угадайте число: "))
        except:
            print("Ошибка!")
            continue

if __name__ == '__main__':
    get_number()
