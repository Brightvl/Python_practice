import csv

phonebook = [{"surname": "Иванов", "name": "Иван", "phone": "79147564729", "description": "Начальник"},
             {"surname": "Иванько", "name": "Сергей", "phone": "79147564465", "description": "Работник"}]


# Чтение телефонного справочника
def read_records(phonebook):
    surname_filter = input("Введите первую часть фамилии для поиска: ").capitalize()
    found_records = []
    for person in phonebook:
        # Startswith Помогает определить начинается ли строка с символов указанных в скобках. Возвращает True or False
        # get возвращает значение по введенному ключу
        if person.get("surname").startswith(surname_filter):
            found_records.append([record_ for data_, record_ in person.items()])
    if found_records:
        print("\nРезультаты поиска:")
        for record in found_records:
            print(f"Имя: {record[0]}, Фамилия: {record[1]}, Телефон: {record[2]}, Описание: {record[3]}")
    else:
        print("Записи не найдены.")


# # Создание новой записи в справочнике
# def create_record(phonebook):
#     name = input("Введите имя: ")
#     surname = input("Введите фамилию: ")
#     phone = input("Введите телефон: ")
#     description = input("Введите описание: ")
#     phonebook[len(phonebook)+1] = (name, surname, phone, description)
#
read_records(phonebook)
