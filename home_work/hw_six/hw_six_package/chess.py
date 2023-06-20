from random import shuffle


def is_attacking(q1, q2):
    if q1[0] == q2[0] or q1[1] == q2[1]:
        return True
    if abs(q1[0] - q2[0]) == abs(q1[1] - q2[1]):
        return True
    return False


def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if is_attacking(queens[i], queens[j]):
                return False
    return True


def random_place():
    col = [1, 2, 3, 4, 5, 6, 7, 8]
    row = [1, 2, 3, 4, 5, 6, 7, 8]
    counter = 0
    rand_result = []
    out = []
    while counter != 4:
        while (queens := list(zip(col, row))) in rand_result:
            shuffle(col)
            shuffle(row)
        rand_result.append(queens)
        if check_queens(queens):
            out.append(queens)
            counter += 1
    else:
        return out


if __name__ == '__main__':
    rand_res = random_place()
    for res in rand_res:
        print(res)
