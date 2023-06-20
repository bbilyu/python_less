from hw_six_package import input_date, check_queens, random_place

if __name__ == '__main__':

    queens_1 = [(8, 7), (2, 3), (3, 7), (3, 3), (7, 3), (8, 2), (5, 5), (4, 3)]
    queens_2 = [(1, 1), (2, 7), (3, 5), (4, 8), (5, 2), (6, 4), (7, 6), (8, 3)]
    queens_rand = random_place()

    print("Задание 1: \n")
    print(input_date())

    print("Задание 2: \n")
    print(check_queens(queens_1))
    print(check_queens(queens_2))

    print("Задание 3: \n")
    for x in queens_rand:
        print(x)
        print(check_queens(x))
