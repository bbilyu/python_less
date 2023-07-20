from string import ascii_lowercase

def removal_chars(text:str) -> str:
    result = ''
    for ch in text.lower():
        if ch in ascii_lowercase + ' ':
            result += ch
    return result

if __name__ == '__main__':
    print(removal_chars("abcdefg"))