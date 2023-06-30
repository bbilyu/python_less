"""Задание №3
Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции."""
import json
from typing import Callable


def json_saver(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('json_saver.json', "a", encoding="utf-8") as f:
            json.dump({result: {"args": args, "kwargs": kwargs}}, f, indent=4)
        return result

    return wrapper


@json_saver
def number_sum(a: float, b: float,round_param) -> float:
    return round(a + b, round_param)


if __name__ == '__main__':
    number_sum(1.22345675, 2.2267,2)
