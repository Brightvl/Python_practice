# №7.3[###]. Имея список вида [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...] преобразовать его
# в списки вида
#
# ['Иванов-И-И', 'Петров-П-П', 'Соколов-И-Г'...]
# ['Иванов И.И.', 'Петров П.П.', 'Соколов И.Г.'...] с использованием Comprehension; Comprehension + функция;
# Comprehension + lambda; map [**] Усложнение. Дополнить обработку списка условием: Выбираем только те элементы,
# в которых первая буква П

from os.path import join


def names_comprehension_one(user_data: list) -> str:
    surname, name, parent = user_data
    return f'{surname} {name[0]}.{parent[0]}.'
    # raise NotImplementedError
    # pass


def names_comprehension_two(surname: str, name: str, parent: str) -> str:
    return f'{surname} {name[0]}.{parent[0]}.'


"привет"

data_path = join('.', 'data')
filename = join(data_path, 'w_07_7.2_data.csv')

with open(filename, mode='r', encoding='utf-8') as file:
    data = [el.strip().split('#') for el in file]
    # print(*data)
    # new_fio = [f'{surname} {name[0]}. {parent[0]}.' for surname, name, parent in data]

    # Comprehension
    # new_fio = [names_comprehension_one(list_data_user) for list_data_user in data]

    # Comprehension
    # new_fio = [names_comprehension_two(*list_data_user) for list_data_user in data]

    #  lambda function
    # new_fio = [(lambda sur_name, first_name, parent_name: f'{sur_name} {first_name[0]}.{parent_name[0]}.')
    #            (surname, name, parent) for surname, name, parent in data]

    # new_fio = list(map(names_comprehension_one, data))

    new_fio = [*map(names_comprehension_one, data)]

print(new_fio)
print(*new_fio)
print(type(new_fio))
