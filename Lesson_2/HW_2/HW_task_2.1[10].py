# 2.1[10]: На столе лежат n монеток. Некоторые из 
# них лежат вверх решкой, а некоторые – 
# гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были 
# повернуты вверх одной и той же стороной. Выведите 
# минимальное количество монет, которые нужно перевернуть. 
# Количество монет и их положение (0 или 1) пользователь 
# вводит с клавиатуры.
#     Примеры/Тесты:
#     Введите кол-во монет>? 5
#     Положение монеты 0: 0 или 1>? 1
#     ...
#     1 0 1 1 0
#     Кол-во монет, чтобы перевернуть: 2

number_coin = 5

for i in number_coin:
    input("Орел:0 или решка:1?" )