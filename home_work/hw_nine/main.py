"""Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке.
100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней квадратного
уравнения с каждой тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты работы
функции в json файл."""

import csv
import json
import math
import random

from typing import Callable


def csv_args(func: Callable):
    out = {}

    def wrapper(**kwargs):
        with open("rand_numbers.csv", 'r', encoding="utf-8") as f:
            csv_read = csv.reader(f)
            for line in csv_read:
                args = [int(arg.replace(" ", "")) for arg in line]
                result = func(*args, **kwargs)
                out[f"{args[0]}x^2+{args[1]}x+{args[2]}"] = result
        return out

    return wrapper


def json_saver(func: Callable):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('json_saver.json', "a", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False)
        return result

    return wrapper


def rand_numbers():
    rand_num = random.randint(100, 1000)
    with open('rand_numbers.csv', "w", newline='') as file:
        csv_write = csv.writer(file, delimiter=' ')
        for _ in range(rand_num):
            num_one, num_two, num_three = [random.randint(1, 100) for _ in range(3)]
            csv_write.writerow(f"{num_one},{num_two},{num_three}")


@json_saver
@csv_args
def solve_quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return "Нет корней"


if __name__ == '__main__':
    a = 2
    b = -7
    c = 3

    rand_numbers()
    solve_quadratic_equation(a, b, c)
