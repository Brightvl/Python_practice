# Путь к файлу
def file_path() -> str:
    return input("\nУкажите путь к файлу (пример: data/data1.txt): ")


# Запрос новых данных в словарь
def get_record():
    return {"surname": input("Введите фамилию: ").capitalize(),
            "name": input("Введите имя: ").capitalize(),
            "phone": input("Введите телефон: "),
            "description": input("Введите описание: ").capitalize()}


# Отображение меню
def menu_buttons() -> str:
    print("(о)Отобразить словарь на экране",
          "(н)Новая запись",
          "(ф)Фильтр по 'Фамилии'",
          "(э)Экспортировать данные в файл",
          "(и)Импортировать данные из файла",
          "(з)Заменить поля выбранной записи",
          "(с)Сохранить изменения в файл",
          "(в)Выход", sep="\n")

    return input("\nВведите нужную букву > ").lower()


def show_list_tuple_dict(data_phonebook):
    if data_phonebook:
        for key, record in data_phonebook:
            print(f"№{key + 1}. Фамилия: {record['surname']}, Имя: {record['name']}, Телефон: {record['phone']}, "
                  f"Описание: {record['description']}")


def show_list_dict(data_phonebook):
    if data_phonebook:
        for idx, record in enumerate(data_phonebook):
            print(f"№{idx + 1}. Фамилия: {record['surname']}, Имя: {record['name']}, Телефон: {record['phone']}, "
                  f"Описание: {record['description']}")


def view_notion(number_notion, separator_start="", separator_end=""):
    notion = {"новая запись": "Новая запись создана в словаре.",
              "пустой справочник": "Ваш телефонный справочник пуст.",
              "ошибка импорта": "Сначала вам нужно импортировать телефонный справочник!",
              "ошибка экспорта": "Нечего экспортировать. Ваш файл пуст.\nПроверьте файл импорта.",
              "данные не найдены": "Данные не найдены, возможно вы не импортировали файл.",
              "экспорт": "Файл экспортирован в указанном пути.",
              "файл не найден": "Файл не найден.",
              "конец программы": "Конец программы"}
    if separator_start:
        separator_start = separator_start * len(notion[number_notion]) + "\n"
    if separator_end:
        separator_end = "\n" + separator_end * len(notion[number_notion])

    return print(f"{separator_start}{notion[number_notion]}{separator_end}")


# def ask_surname(default_value: str = ""):
#     return input(f"Введите фамилию {f'({default_value})' if default_value else ''} > ") or default_value

def create_new_file(export_file_path: str) -> str:
    view_notion("файл не найден")
    return input(f"Создать eго в указанном пути? <{export_file_path}> Y/N: ").upper()
