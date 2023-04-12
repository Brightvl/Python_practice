№3.1[17]. Дан список чисел. Определите, сколько в нем встречается различных чисел.

Примечание: Пользователь может вводить значения списка или список задан изначально.

Примеры/Тесты:

[1, 1, 2, 0, -1, 3, 4, 4] -> 6

[1, 1, 2, 0, 1, 2, 1, 2] -> 3

№3.2[19]. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

Примечание: Пользователь может вводить значения списка или список задан изначально.

Примеры/Тесты:

Input: [1, 2, 3, 4, 5] k = 3

Output: [4, 5, 1, 2, 3]

№3.3[21]. Напишите программу для печати всех уникальных значений в списке словарей.

Примечание: Список словарей задан изначально. Пользователь его не вводит

Обратите внимание, что в словарях может быть один или несколько элементов

Примеры/Тесты:

Input: [{"V": "S001", "X": "D009"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005", "XI": "D011"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 ", "XII": "D001"}]

Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

[*] Усложнение. Проверку уникальности строк сделайте без учета пробелов до и после значимой части строки

[**] Усложнение. Запишите алгоритм в одну строку, используйте Comprehension

№3.4[23]. Дан список, состоящий из целых чисел. Напишите программу, которая сформирует список из тех элементов, которые больше предыдущего (элемента с предыдущим номером)

Примечание: Пользователь может вводить значения списка или список задан изначально.

Примеры/Тесты:

Input: [0, -1, 5, 2, 1]

Output: [5]

Input: [-2, -1, 5, 2, 3]

Output: [-1, 5, 3]

[*] Усложнение: Запишите алгоритм в одну строку, используйте Comprehension

print (element for index_elements in range(len(element)) if element[index_elements] > element[index_elements -1])