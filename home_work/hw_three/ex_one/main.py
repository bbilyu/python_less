"""Дан список повторяющихся элементов. Вернуть список
с дублирующимися элементами. В результирующем списке
не должно быть дубликатов"""

def remove_duplicates(lst):
    new_lst = []
    for item in lst:
        if lst.count(item) > 1 and item not in new_lst:
            new_lst.append(item)
    return new_lst

if __name__ == '__main__':
    lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    print(remove_duplicates(lst))
