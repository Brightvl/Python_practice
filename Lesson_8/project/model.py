from view import get_record


# Создание новой записи в справочнике
def create_record(data_phonebook: list):
    # Запрос у пользователя данных для добавления в справочник
    return data_phonebook.append(get_record())


# фильтр в справочнике по фамилии
def filter_records_surname(data_phonebook) -> list:
    surname_filter = input("Введите первую часть фамилии для поиска: ").capitalize()
    found_records = []
    for idx, person in enumerate(data_phonebook):
        # Startswith Помогает определить начинается ли строка с символов указанных в скобках. Возвращает True or False
        # get возвращает значение по введенному ключу
        if person.get("surname").startswith(surname_filter):
            found_records.append((idx, person))
    return found_records


# update Изменение полей выбранной записи
def change_records(data_phonebook):
    surname_filter = input("Введите первую часть фамилии для поиска: ").capitalize()
    found_records = []
    for idx, person in enumerate(data_phonebook):
        # Startswith Помогает определить начинается ли строка с символов указанных в скобках. Возвращает True or False
        # get возвращает значение по введенному ключу
        if person.get("surname").startswith(surname_filter):
            found_records.append([idx, person])
    if len(found_records) != 0:
        print("\nРезультаты поиска")
        for record in found_records:
            key = record[0]  # Небольшая распаковка списка списков
            element = record[1]
            print(f"№{key + 1}. Фамилия: {element['surname']}, Имя: {element['name']}, Телефон: {element['phone']}, "
                  f"Описание: {element['description']}")

    if len(found_records) == 1:
        # Получаем индекс записи в нашем списке
        record_number = found_records[0][0]
        # добавляем функцию get record и перезаписываем данные
        print("—————————————————————\n"
              "Введите новые данные:")
        data_phonebook[record_number] = get_record()
    elif len(found_records) > 1:
        record_number = int(input("——————————————————————————————————————————————————\n"
                                  "Найдено несколько позиций удовлетворяющих фильтру.\n"
                                  "Укажите номер нужного человека: ")) - 1
        data_phonebook[record_number] = get_record()
    else:
        print("————————————————————————————————\n"
              "Человек в справочнике не найден!"
              "\n————————————————————————————————")


# Экспорт файла
def export_in_file(export_file, data):
    # w - запись
    with open(export_file, "w", encoding='utf-8') as file:
        for el in data:  # перебор строк в файле + \n
            file.write(f"{el['surname']},{el['name']},{el['phone']},{el['description']}\n")


# импорт справочника из файла и добавление его в список для обработки (чтобы сохранить его в памяти)
def read_file(file_path: str) -> list:
    data = []
    # r тип операции - чтение
    with open(file_path, "r", encoding='utf-8') as file:
        for string in file:  # перебор строк в файле + \n
            new_list = string.strip().split(",")  # убираем перенос строки и делим по запятой
            data.append({"surname": new_list[0], 'name': new_list[1], 'phone': new_list[2], 'description': new_list[3]})
    return data


# Удаление файла
def delete_records():
    raise NotImplementedError
