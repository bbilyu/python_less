"""
Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.

"""

import os


def split_path(file_path):
    path, filename = os.path.split(file_path)
    name, ext = os.path.splitext(filename)
    return path, name, ext


if __name__ == '__main__':
    file_path = "K:/python_lessons/home_work/hw_five/ex_one/test.txt"
    path, name, ext = split_path(file_path)
    print("Путь:", path)
    print("Имя файла:", name)
    print("Расширение файла:", ext)