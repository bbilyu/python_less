"""
Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.
"""


def make_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            hash(value)
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result


if __name__ == '__main__':
    result = make_dict(a=1, b="hello", c=[1, 2, 3], d={"key": "value"})
    print(result)
