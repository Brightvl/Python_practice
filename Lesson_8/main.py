# Для поиска файла в системе
import os


# Путь к файлу
def file_path() -> str:
    return input("\nУкажите путь к файлу (пример: data/data1.txt): ")


# Проверка пути
def path_check(file_path: str) -> bool:
    if os.path.isfile(file_path):
        return True
    else:
        return False


# Запрос новых данных в словарь
def get_record():
    return {"surname": input("Введите фамилию: ").capitalize(),
            "name": input("Введите имя: ").capitalize(),
            "phone": input("Введите телефон: "),
            "description": input("Введите описание: ").capitalize()}


# 1. Создание новой записи в справочнике
def create_record(data_phonebook: list):
    # Запрос у пользователя данных для добавления в справочник
    return data_phonebook.append(get_record())


# 2. Вывод справочника на экран
def view_phonebook(data_phonebook):
    print("\nДанные справочника:")
    temp = 1
    for string in data_phonebook:
        print(f"{temp}) Фамилия: {string['surname']}, Имя: {string['name']}, Телефон: {string['phone']}, Описание: "
              f"{string['description']}")
        temp += 1


# 3. фильтр в справочнике по фамилии
def read_records_surname(data_phonebook):
    surname_filter = input("Введите первую часть фамилии для поиска: ").capitalize()
    found_records = []
    for person in data_phonebook:
        # Startswith Помогает определить начинается ли строка с символов указанных в скобках. Возвращает True or False
        # get возвращает значение по введенному ключу
        if person.get("surname").startswith(surname_filter):
            found_records.append([record_ for data_, record_ in person.items()])
    if found_records:
        print("——————\nРезультаты поиска:")
        temp = 1
        for record in found_records:
            print(f"{temp}) Фамилия: {record[0]}, Имя: {record[1]}, Телефон: {record[2]}, Описание: {record[3]}")
            temp += 1
    else:
        print("Записи не найдены.")


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


# 4. Экспорт в файл
def export_in_file(export_file, data):
    with open(export_file, "w", encoding='utf-8') as file:
        for el in data:  # перебор строк в файле + \n
            file.write(f"{el['surname']},{el['name']},{el['phone']},{el['description']}\n")


# 5. импорт справочника из файла и добавление его в список для обработки (чтобы сохранить его в памяти)
def read_file(file_path: str) -> list:
    data = []
    # r тип операции - чтение
    with open(file_path, "r", encoding='utf-8') as file:
        for string in file:  # перебор строк в файле + \n
            new_list = string.strip().split(",")  # убираем перенос строки и делим по запятой
            data.append({"surname": new_list[0], 'name': new_list[1], 'phone': new_list[2], 'description': new_list[3]})
    return data


# Сохранение файла
# def save_file(export_file, data):
#     with open(export_file, "w", encoding='utf-8') as file:
#         for el in data:  # перебор строк в файле + \n
#             file.write(f"{el['surname']},{el['name']},{el['phone']},{el['description']}\n")


# Объект список который хранит в себе данные телефонного справочника
phonebook = []

# Меню программы
while True:
    print("\nВозможные действия")
    print("1. Вывести словарь на экран")
    print("2. Создать запись")
    print("3. Вывести имеющиеся данные по фильтру 'Фамилия'")
    print("4. Экспортировать данные в файл")
    print("5. Импортировать данные из файла")
    print("6. Выход")

    print("7. Изменить поля выбранной записи")
    print("8. Сохранить изменения в файл")

    user_input = input("\nВведите действие > ")

    # 1. Вывести словарь на экран
    if user_input == "1":
        if len(phonebook) == 0:
            print("\nДанные не найдены, возможно вы не импортировали файл.")
        else:
            view_phonebook(phonebook)
    # 2. Создать запись
    if user_input == "2":
        if len(phonebook) != 0:
            create_record(phonebook)
            print("———————————————————————————————\n"
                  "Новая запись создана в словаре."
                  "\n———————————————————————————————")
        else:
            print("——————————————————————————————————————————————————————\n"
                  "Сначала вам нужно импортировать телефонный справочник!"
                  "\n——————————————————————————————————————————————————————")
    # 3. Вывести имеющиеся данные по фильтру 'Фамилия'
    if user_input == "3":
        if len(phonebook) != 0:
            read_records_surname(phonebook)
        else:
            print("————————————————————————————————————\n"
                  "Ваш телефонный справочник пуст.\n"
                  "Возможно вы забыли его импортировать."
                  "\n————————————————————————————————————")
    # 4. Экспортировать данные в файл
    if user_input == "4":
        if len(phonebook) != 0:
            export_file_path = file_path()
            if path_check(export_file_path):
                # Экспортируем файл(путь к файлу и импортированный список PB)
                export_in_file(export_file_path, phonebook)
                print(f"————————————————————————————————————\n"
                      f"Файл экспортирован в указанном пути.\n"
                      f"Путь: {export_file_path}"
                      f"\n————————————————————————————————————")
            else:
                temp = input(f"файл не найден\n"
                             f"Создать eго в указанном пути? <{export_file_path}> Y/N: ").upper()
                if temp == "Y":
                    export_in_file(export_file_path, phonebook)
                    print(f"————————————————————————————————————\n"
                          f"Файл экспортирован в указанном пути.\n"
                          f"Путь: {export_file_path}"
                          f"\n————————————————————————————————————")
        else:
            print("—————————————————————————————————————\n"
                  "Нечего экспортировать. Ваш файл пуст.\n"
                  "Проверьте файл импорта."
                  "\n—————————————————————————————————————")
    # 5. Импортировать данные из файла
    if user_input == "5":
        # import_file_path = file_path()
        import_file_path = "data/data1.txt"
        if path_check(import_file_path):  # Проверка указанного пути
            # Чтение файла
            phonebook = read_file(import_file_path)
            print(f"——————————————————\nФайл импортирован\n——————————————————")
        else:
            print("\nПуть к файлу указан неправильно!")
    # 6. Выход
    if user_input == "6":
        print("———————————————\n"
              "Конец программы"
              "\n———————————————")
        break

    # 7. Изменить поля выбранной записи
    if user_input == "7":
        if len(phonebook) != 0:
            if input("Вывести словарь на экран? 'Y-Yes' если нет, нажмите 'Enter'").upper() == "Y":
                view_phonebook(phonebook)
            change_records(phonebook)




        else:
            print("————————————————————————————————————\n"
                  "Ваш телефонный справочник пуст.\n"
                  "Возможно вы забыли его импортировать."
                  "\n————————————————————————————————————")

    # Сохранить файл
    # if user_input == "8":
    #     if len(phonebook) != 0:
    #         if path_check(import_file_path):
    #             # Экспортируем файл(путь к файлу и импортированный список PB)
    #             export_in_file(export_file_path, phonebook)
    #             print(f"————————————————————————————————————\n"
    #                   f"Файл экспортирован в указанном пути.\n"
    #                   f"Путь: {export_file_path}"
    #                   f"\n————————————————————————————————————")
    #         else:
    #             temp = input(f"файл не найден\n"
    #                          f"Создать eго в указанном пути? <{export_file_path}> Y/N: ").upper()
    #             if temp == "Y":
    #                 export_in_file(export_file_path, phonebook)
    #                 print(f"————————————————————————————————————\n"
    #                       f"Файл экспортирован в указанном пути.\n"
    #                       f"Путь: {export_file_path}"
    #                       f"\n————————————————————————————————————")
    #     else:
    #         print("—————————————————————————————————————\n"
    #               "Вы пытаетесь сохранить пустой файл"
    #               "Проверьте импортировали ли вы его"
    #               "\n—————————————————————————————————————")
