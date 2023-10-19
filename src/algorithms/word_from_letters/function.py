import time

import pymorphy3


LENGTH_LIMIT = 7
"""Предельная длина строки"""
WORDS = 'words'
"""Ключ для словаря с результатом работы функции main"""


def generate_permutations(letters_str: str) -> list[str]:
    """Генерирует все варианты перестановок символов указанной строки
    :param letters_str: входящая строка
    :return: список перестановок символов входящей строки, где каждая
    перестановка строка, содержащая указанные символы
    """
    if not isinstance(letters_str, str):
        raise TypeError('Переданный параметр не является строкой')
    if len(letters_str) > LENGTH_LIMIT:
        raise ValueError('Длина введенной строки превышает '
                         f'{LENGTH_LIMIT} символов')
    if ' ' in letters_str:
        raise ValueError('Введенная строка содержит пробел')

    letters_str = letters_str.lower()

    def permute(data, i, length):
        if i == length:
            yield ''.join(data)
        else:
            for j in range(i, length):
                data[i], data[j] = data[j], data[i]
                yield from permute(data, i+1, length)
                data[i], data[j] = data[j], data[i]

    return list(permute(list(letters_str), 0, len(letters_str)))


def main(letters: str):
    """Генерирует слова, составленные из символов входящей строки. Из символов
    генерируются все возможные перестановки, которые проверяются через словарь
    с помощью библиотеки pymorphy3
    :param letters: входящая строка
    :raise TypeError: если параметр не является строкой
    :raise ValueError: если входящая строка содержит пробел или ее длина
    превышает максимально возможное значение
    :return: список слов
    """
    morph = pymorphy3.MorphAnalyzer()
    permutations = set(generate_permutations(letters))
    words = []
    for permutation in permutations:
        if morph.word_is_known(permutation):
            words.append(permutation)
    return {WORDS: words}


if __name__ == '__main__':
    letters = 'abc'
    print(generate_permutations(letters))

    start_time = time.time()
    letters = 'Поледар'
    print(main(letters))
    print(f'duration: {time.time() - start_time} seconds')
