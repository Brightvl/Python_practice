# 3.2[18]: Требуется найти в списке целых чисел самый
# близкий по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список
# можно считать заданным. Введенное число не обязательно
# содержится в списке.

#     Примеры/Тесты:
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
#     Output: 2
#     Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9

list_num = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
list_num.sort()
x = 4
# set_num = set(list_num)
# print(set_num)

diff_num = abs(x - list_num[0])
min_num = list_num[0]

for el in list_num:
    raznica = abs(x - el)
    # print(f"{el}, {raznica} < {diff_num} = {raznica < diff_num}")
    if raznica < diff_num:
        diff_num = raznica
        min_num = el
print(min_num)

