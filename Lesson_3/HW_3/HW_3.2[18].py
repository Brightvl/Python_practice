# 3.2[18]: Требуется найти в списке целых чисел самый
# близкий по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список
# можно считать заданным. Введенное число не обязательно
# содержится в списке.

#     Примеры/Тесты:
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
#     Output: 2
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9

# Не судите строго, просто практикуюсь 

# В функцию передаем список и искомое число
def nearest_number(lst, find_number):
    # в множество и наоборот и сортируем по порядку
    lst = sorted(list(set(lst))) 
    # Переменная для хранения минимальной разности искомого и эл-та списка
    min_diff = abs(find_number - lst[0])
    min_num_of_lst = lst[0] # Для определение 1 ближайшего в lst
    min_num_of_lst_2 = lst[0] # Для определение 2-го ближайшего
    
    for el in lst: # Перебираем список 
        # для нахождения min разности, определяем разницу для каждого эл-та списка
        loop_difference = abs(find_number - el) 
        # Если найдена меньшая разность, записываем в min и запоминаем число
        if loop_difference < min_diff:
            min_diff = loop_difference
            min_num_of_lst = el
        # Для того чтобы проверить есть ли второе ближайшее число
        if  loop_difference == min_diff and min_num_of_lst != el: min_num_of_lst_2 = el
        # Если его нет, присваиваю пустую строку
        if min_num_of_lst_2 == lst[0]: min_num_of_lst_2 = ''
    print(f"Ближайшие значения к числу '{find_number}' -> {min_num_of_lst}  {min_num_of_lst_2}")

number_list = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
nearest_number(number_list, 6)

# Клевый код от Бори (лучше моего)
# numbers = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
# input_number = 3

# closest_numbers = [numbers[0]]
# difference = abs(input_number - closest_numbers[0])

# for number in numbers:
#     new_difference = abs(input_number - number)
#     if new_difference < difference:
#         closest_numbers = [number]
#         difference = abs(input_number - number)
#     elif new_difference == difference:
#         closest_numbers.append(number)

# print(set(closest_numbers))

# изначальное решение
# list_num.sort()
# x = 4
# diff_num = abs(x - list_num[0])
# min_num = list_num[0]

# for el in list_num:
#     raznica = abs(x - el)
#     # print(f"{el}, {raznica} < {diff_num} = {raznica < diff_num}")
#     if raznica < diff_num:
#         diff_num = raznica
#         min_num = el
# print(min_num)

