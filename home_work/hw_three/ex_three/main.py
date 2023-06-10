"""Создайте словарь со списком вещей для похода в качестве
ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную
грузоподъёмность. Достаточно вернуть один допустимый вариант."""


def get_items_backpack(max_weight, items: dict):
    sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
    backpack_items = []
    remaining_weight = max_weight

    for item, weight in sorted_items:

        if weight <= remaining_weight:
            backpack_items.append(item)
            remaining_weight -= weight

    return backpack_items

if __name__ == '__main__':
    print(get_items_backpack(10, {"ложка": 3, "нож": 7, ",бумбокс": 1, "вилка": 11}))
