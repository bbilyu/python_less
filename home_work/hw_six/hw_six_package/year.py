def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_valid_date(date):
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 9999 and 1 <= month <= 12:
        if month == 2:
            if is_leap_year(year):
                return 1 <= day <= 29
            else:
                return 1 <= day <= 28
        elif month in [4, 6, 9, 11]:
            return 1 <= day <= 30
        else:
            return 1 <= day <= 31
    else:
        return False


def input_date():
    while True:
        try:
            date_in = input("Введите дату в формате дд.мм.гггг: ")
            if len(date_in.split('.')) != 3:
                raise Exception
            return is_valid_date(date_in)
        except:
            print("Ошибка!")
            continue


if __name__ == '__main__':
    print(is_valid_date('22.12.1986'))
    print(is_valid_date('29.2.2023'))
    print(is_valid_date('29.2.2020'))
    print(is_valid_date('32.2.2020'))
    input_date()
