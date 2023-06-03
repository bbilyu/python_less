from random import randint

"""
1.Решить задачи, которые не успели решить на семинаре:
a. Написать программу, которая будет выводить в консоль ёлочку заданной высоты
б. Написать порграмму, которая выодит в консоль таблицу умножения "как на тетрадках"
"""


def get_tree(row):
    START_VALUE = 1
    SPACE = row - 1
    print(SPACE * " ", "*" * START_VALUE)
    if row != 1:
        for x in range(row - 1):
            START_VALUE += 2
            SPACE -= 1
            print(SPACE * " ", "*" * START_VALUE)


# get_tree(20)

def print_base(x, y, num):
    if y != num:
        print(f"{y} * {x} = {x * y:2}", end="      ")

    else:
        print(f"{y} * {x} = {x * y}")


def get_multiplication_table():
    for i in range(2, 10):
        for j in range(2, 6):
            print_base(i, j, 5)
    print("\n")
    for i in range(2, 10):
        for j in range(6, 10):
            print_base(i, j, 9)


# get_multiplication_table()

"""
2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны
предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в
одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно
сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""


def get_side(number):
    return int(number)


def check_triangle(a, b, c):
    if a < (b + c) and b < (a + c) and c < (a + b):
        if a == b == c:
            print("Треугольник равносторонний")
        elif (a == b) or (b == c) or (c == a):
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")

    else:
        print("Треугольник не существует")


def ex_two():
    while True:
        try:
            side_a = get_side(input("Введите значние стороны a: "))
            side_b = get_side(input("Введите значние стороны b: "))
            side_c = get_side(input("Введите значние стороны c: "))
            check_triangle(side_a, side_b, side_c)
            break
        except ValueError:
            print("Пожалуйста введите целое число!")
            continue


# ex_two()


"""
3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для
проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод
отрицательных чисел и чисел больше 100 тысяч. 
"""


def compound_simple(number):
    num = int(number)
    if num < 0 or num > 100000:
        raise Exception("Введите число больше нуля и меньше 100000!!!")
    count = 0
    for x in range(1, num + 1):
        if num % x == 0:
            count += 1
    return print("Число простое") if count == 2 else print("Число составное")


def ex_three():
    while True:
        try:
            compound_simple(input("Введите число: "))
            break
        except ValueError:
            print("Повторите попытку!")
            continue
        except Exception as e:
            print(e)
            continue


# ex_three()

"""4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать 
«больше» или «меньше» после каждой попытки. """


def ex_four():
    user_num = None
    LOWER_LIMIT = 0
    UPPER_LIMIT = 1000
    NUMBER_ATTEMPTS = 10
    rand_num = randint(LOWER_LIMIT, UPPER_LIMIT)
    print(f"Угадайте число за {NUMBER_ATTEMPTS} попыток")
    for x in range(NUMBER_ATTEMPTS):
        NUMBER_ATTEMPTS -= 1
        while True:
            try:
                user_num = int(input("Введите целое число: "))
                break
            except ValueError:
                print("Ошибка!Пожалуйста введите целое цисло!")
                continue
        if user_num == rand_num:
            return print("Поздравляем вы угадали число!")
        elif user_num > rand_num:
            print(f"Осталось попыток: {NUMBER_ATTEMPTS}")
            print(f"Загаданное число меньше вашего!")
        elif user_num < rand_num:
            print(f"Осталось попыток: {NUMBER_ATTEMPTS}")
            print(f"Загаданное число больше вашего!")
    return print("К сожалению вы проиграли :(")


ex_four()
