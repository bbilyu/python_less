"""Задание №8
Погружение в Python | Коллекции
✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей."""

if __name__ == '__main__':
    friends_items = {
        'Коля': ('тент', 'спальный мешок', 'рюкзак', 'бубмокс'),
        'Вася': ('тент', 'спальный мешок', 'рюкзак', 'бубмокс','карта'),
        'Петя': ('тент', 'спальный мешок', 'рюкзак', 'бубмокс', 'карта')
    }


    all_items = set.intersection(*map(set, friends_items.values()))
    print('Вещи, которые взяли все три друга:', all_items)


    unique_items = set.union(*map(set, friends_items.values())) - all_items
    print('Уникальные вещи:', unique_items)



    for item in unique_items:
        friends_with_item = [friend for friend, items in friends_items.items() if item in items]
        if len(friends_with_item) < len(friends_items):
            missing_friend = set(friends_items.keys()) - set(friends_with_item)
            print(f'Вещь "{item}" есть у всех кроме {missing_friend.pop()}')