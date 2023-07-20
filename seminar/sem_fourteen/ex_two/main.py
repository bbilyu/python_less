
# Задание №2
# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)



from string import ascii_lowercase


def removal_chars(text: str) -> str:
    """
    >>> removal_chars('abcdefg')
    'abcdefg'
    >>> removal_chars('ABCDEFG')
    'abcdefg'
    >>> removal_chars('a,b,c,d,e,f,g')
    'abcdefg'
    >>> removal_chars('aаbбcвdгeдfеg')
    'abcdefg'
    >>> removal_chars('Aа,Bбcвdгeдfеg')
    'abcdefg'
    """
    result = ''
    for ch in text.lower():
        if ch in ascii_lowercase + ' ':
            result += ch
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
