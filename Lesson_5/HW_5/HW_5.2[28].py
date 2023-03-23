# 5.2[28]: Напишите рекурсивную функцию
# sum(a, b), возвращающую сумму двух
# целых неотрицательных чисел. Из
# всех арифметических операций допускаются
# только +1 и -1. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3


def recursion(num_a: int, num_b: int) -> int:
    if not (isinstance(num_a, int) and isinstance(num_b, int)):
        return None
    if num_b == 0: return num_a
    return recursion(num_a, num_b-1) + 1

print(recursion(5, 10))
print(recursion(4, "et"))
