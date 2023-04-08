import os

from model import create_record, filter_records_surname, export_in_file, read_file, change_records
from view import file_path, menu_buttons, view_notion, show_list_tuple_dict, show_list_dict, create_new_file


# Меню программы
def menu(data_phonebook):
    while True:
        user_input = menu_buttons()

        # Вывести словарь на экран
        if user_input == "о":
            if len(data_phonebook) == 0:
                view_notion("данные не найдены")
            else:
                show_list_dict(data_phonebook)
        # Новая запись
        if user_input == "н":
            if len(data_phonebook) != 0:
                create_record(data_phonebook)
                view_notion("новая запись", separator_end="—")
            else:
                view_notion("ошибка импорта")
        # Вывести имеющиеся данные по фильтру 'Фамилия'
        if user_input == "ф":
            surname_filter = filter_records_surname(data_phonebook)
            if len(surname_filter) != 0:
                show_list_tuple_dict(surname_filter)
            else:
                view_notion("пустой справочник")
        # Экспортировать данные в файл
        if user_input == "э":
            if len(data_phonebook) != 0:
                export_file_path = file_path()
                if path_check(export_file_path):
                    # Экспортируем файл(путь к файлу и импортированный список PB)
                    export_in_file(export_file_path, data_phonebook)
                    view_notion("экспорт")
                else:
                    choice = create_new_file(export_file_path)
                    if choice == "Y":
                        export_in_file(export_file_path, data_phonebook)
                        view_notion("экспорт", "-", "-")
            else:
                view_notion("ошибка экспорта", "-", "-")
        # Импортировать данные из файла
        if user_input == "и":
            # import_file_path = file_path()
            import_file_path = "data/data1.txt"
            if path_check(import_file_path):  # Проверка указанного пути
                # Чтение файла
                data_phonebook = read_file(import_file_path)
                print(f"——————————————————\nФайл импортирован\n——————————————————")
            else:
                print("\nПуть к файлу указан неправильно!")
        # Выход
        if user_input == "в":
            view_notion("конец программы")
            break
        # Изменить поля выбранной записи
        if user_input == "з":
            if len(data_phonebook) != 0:
                if input("Вывести словарь на экран? 'Y-Yes' если нет, нажмите 'Enter'").upper() == "Y":
                    view_phonebook(data_phonebook)
                change_records(data_phonebook)
            else:
                print("————————————————————————————————————\n"
                      "Ваш телефонный справочник пуст.\n"
                      "Возможно вы забыли его импортировать."
                      "\n————————————————————————————————————")


# Проверка пути
def path_check(file_path: str) -> bool:
    if os.path.isfile(file_path):
        return True
    else:
        return False

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
