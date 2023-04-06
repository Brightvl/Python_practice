import os


# Путь к файлу
def file_path() -> str:
    return input("\nУкажите путь к файлу: ")


# Проверка пути
def path_check(file_path) -> bool:
    if os.path.isfile(file_path):
        return True
    else:
        return False


# Создание новой записи в справочнике
def create_record(data_phonebook):
    new_person = {}
    new_person["surname"] = input("\nВведите фамилию: ").capitalize()
    new_person["name"] = input("Введите имя: ").capitalize()
    new_person["phone"] = input("Введите телефон: ")
    new_person["description"] = input("Введите описание: ").capitalize()
    return data_phonebook.append(new_person)


# Чтение файла и запись в список, чтобы сохранить его в памяти
def read_file(file_path: str) -> list:
    data = []
    # r тип операции - чтение
    with open(file_path, "r", encoding='utf-8') as file:
        for string in file:  # перебор строк в файле + \n
            new_list = string.strip().split(",")  # убираем перенос строки и делим по запятой
            data.append({"surname": new_list[0], 'name': new_list[1], 'phone': new_list[2], 'description': new_list[3]})
    return data


# Вывод справочника на экран
def view_phonebook(data_phonebook):
    print("\nДанные справочника:")
    for string in data_phonebook:
        print(f"Фамилия: {string['surname']}, Имя: {string['name']}, Телефон: {string['phone']}, Описание: "
              f"{string['description']}")


# фильтр в справочнике по фамилии
def read_records_surname(data_phonebook):
    surname_filter = input("Введите первую часть фамилии для поиска: ").capitalize()
    found_records = []
    for person in data_phonebook:
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


# Экспорт в файл
def export_in_file(export_file, data):
    with open(export_file, "w", encoding='utf-8') as file:
        for el in data:  # перебор строк в файле + \n
            file.write(f"{el['surname']},{el['name']},{el['phone']},{el['description']}\n")


phonebook = []
while True:
    print("\nВозможные действия")
    print("1. Создать запись")
    print("2. Вывести имеющиеся данные")
    print("3. Экспортировать данные в файл")
    print("4. Импортировать данные из файла")
    print("5. Выход")
    user_input = input("\nВведите действие > ")

    if user_input == "1":
        create_record(phonebook)
    if user_input == "2":
        if len(phonebook) == 0:
            print("\nДанные не найдены, проверьте импортировали ли вы список")
        else:
            view_phonebook(phonebook)
    if user_input == "3":
        if len(phonebook) != 0:
            export_file_path = file_path()
            if path_check(export_file_path):
                # Чтение файла
                export_in_file(export_file_path, phonebook)
            else:
                temp = input(f"файл не найден\nСоздать eго в указанном пути? {export_file_path} Y/N: ").upper()
                if temp == "Y":
                    export_in_file(export_file_path, phonebook)
        else:
            print("Вы еще ничего не создали! Проверьте импорт.")
    if user_input == "4":
        import_file_path = file_path()
        if path_check(import_file_path):
            # Чтение файла
            phonebook = read_file(import_file_path)
        else:
            print("\nПуть указан неправильно!")
    if user_input == "5":
        print("_______________\nКонец программы")
        break
