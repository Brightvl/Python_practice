import csv

phonebook = [{"surname": "Иванов", "name": "Иван", "phone": "79147564729", "description": "Начальник"},
             {"surname": "Иванько", "name": "Сергей", "phone": "79147564465", "description": "Работник"}]


# Отображение справочника?

# Чтение телефонного справочника по фильтру
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


# Создание новой записи в справочнике
def create_record(phonebook):
    new_person = {}
    new_person["Name"] = input("Введите фамилию: ").capitalize()
    new_person["surname"] = input("Введите имя: ").capitalize()
    new_person["phone"] = input("Введите телефон: ")
    new_person["description"] = input("Введите описание: ").capitalize()
    return phonebook.append(new_person)


# read_records(phonebook)
create_record(phonebook)
print(phonebook)
