"""
Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии

"""


def calculate_bonus(names, rates, bonuses):
    return {name: rate * float(bonus.strip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)}


if __name__ == '__main__':
    names = ['Alice', 'Bob', 'Charlie']
    rates = [1000, 2000, 3000]
    bonuses = ['5%', '10%', '15%']

    result = calculate_bonus(names, rates, bonuses)
    print(result)
