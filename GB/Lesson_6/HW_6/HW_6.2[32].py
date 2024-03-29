# 6.2[32]: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
# Напишите функцию
# - Аргументы: список чисел и границы диапазона
# - Возвращает: список индексов элементов (смотри условие)
#
# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
# <function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
# <function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]
# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension
#
# (**) Усложнение. Функция возвращает список кортежей вида: индекс, значение
#
# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)]

from random import randint


# В цикле перебираем по порядку для того чтобы потом выводить индексы. Выводятся при условии нахождения числа между
# start и end. Создается список с помощью comprehension
def find_index_range(list_, start, end):
    return [n for n in range(len(list_)) if start <= list_[n] <= end]


# Для вывода кортежа вида индекс значение
def find_in_list(list_, start, end):
    return [(n, list_[n]) for n in range(len(list_)) if start <= list_[n] <= end]


def find_in_list1(list_, start, end):
    return [(idx, el) for idx, el in enumerate(list_) if start <= el <= end]


lst1 = [randint(-20, 20) for el in range(20)]

start_el, end_el = map(int, input(f"Принятый список:\n"
                                  f"{lst1}\n"
                                  f"Введите диапазон чисел для поиска\n"
                                  f"<от> <до>\n").split())

print(f"Индексы чисел в диапазоне: \n{find_index_range(lst1, start_el, end_el)}\n"
      f"Список картежей [(индекс,элемент)]:\n{find_in_list(lst1, start_el, end_el)}\n"
      f"{find_in_list1(lst1, start_el, end_el)}")
