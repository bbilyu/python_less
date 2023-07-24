# Функция получает на вход текст вида: “1-й четверг ноября”, “3я среда мая” и т.п.
# 📌 Преобразуйте его в дату в текущем году.
# 📌 Логируйте ошибки, если текст не соответсвует формату.
# 📌 Добавьте возможность запуска из командной строки.
# 📌 При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
# 📌 Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.

import logging
import sys
from datetime import datetime, date


logging.basicConfig(filename='parse_date.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} функция "{funcName}()" строка {lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

months = {'янв': 1, 'фев': 2, 'мар': 3, 'апр': 4, 'мая': 5, 'июн': 6, 'июл': 7, 'авг': 8, 'сен': 9, 'окт': 10, 'ноя': 11, 'дек': 12}
weekdays = {'пон': 1, 'вто': 2, 'сре': 3, 'чет': 4, 'пят': 5, 'суб': 6, 'вос': 7}

def parse_date(text: str):
    '''Переводим текст в объект дату'''
    try:
        year = datetime.now().year
        count, weekday_, month_ = text.split()

        if count.isdigit():
            count = int(count)
        else:
            count = 1

        if month_.isdigit():
            month = int(month_)
        else:
            month = months[month_[:3]]

        if weekday_.isdigit():
            weekday = int(weekday_)
        else:
            weekday = weekdays[weekday_[:3]] - 1

    except Exception as exc:
        logger.info(f'{count}-й  {weekday_}  {month_} {year} =  ошибка: {exc}')
        return

    count_week = 0
    for day in range(1, 31 + 1):
        rezult = date(year=year, month=month, day=day)
        if rezult.weekday() == weekday:
            count_week += 1
            if count_week == count:
                logger.info(f'{count}-й {weekday_} {month_} {year} = {rezult} ')
                return rezult


if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
        print('Результат:', parse_date(input_text))
    else:
        print('Результат:', parse_date(input("Ввод: ")))
        print('Результат "3я среда 5" :', parse_date("3я среда 5"))