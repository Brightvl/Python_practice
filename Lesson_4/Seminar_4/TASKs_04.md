№4.1[25]. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n.

Примеры/Тесты:
    Input: a a a b c a a d c d d
    Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

    Input: a b c d a a a a a a a
    Output: a b c d a_1 a_2 a_3 a_4 a_5 a_6 a_7

Строку не обязательно вводить с клавиатуры


№4.2[27]. Дана строка, состоящая из слов. Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов.
Слово не зависит от регистра написания букв.
Определите, сколько различных слов содержится в этом тексте.

Примеры/Тесты:
    Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
    Output: 14

    Input: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur a tellus ut arcu gravida porta eget a lacus. Curabitur ornare varius turpis, ultricies mollis sem convallis in. Nunc scelerisque lacinia risus sit amet aliquam.
    Output: 31

[*]  Усложнение. Выведите кол-во слов с учетом регистра и без учета регистра

№4.3[29]. Для натурального n создать список, состоящий из элементов последовательности 3n + 1.
    
    Пример:
    - Для n = 6: [1, 4, 7, 10, 13, 16, 19]
    
    Усложнение:
    Создать список, где указанные числа будут стоять на соответствующих индексах, остальные элементы сделать нулевыми, т.е. для индекса 1, значение 1, 
    для индекса 4, значение 4 и т.п.
    Пример:
    - Для n = 6: [0,1,0,0,4,0,0,7,0,0,10]