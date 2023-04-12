# 3.1[17]. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Примечание: Пользователь может вводить значения списка или список задан изначально.
# Примеры/Тесты:
# [1, 1, 2, 0, -1, 3, 4, 4] -> 6
# [1, 1, 2, 0, 1, 2, 1, 2] -> 3

elements = [1, 1, 2, 0, 1, 2, 1, 2]
num_el = len(elements)

# result = [elements[0]]

# for el in elements:
#     for idx in range(num_el):
#         if el == elements[idx]:
#             continue
#         else:

print(len(set(elements)))

