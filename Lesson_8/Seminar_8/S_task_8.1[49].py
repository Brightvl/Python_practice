# №8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
# Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller

# fio = {'Иванов Иван': ['897097','работник'], 'Петров Петр': ['35346', 'не раб']}
# fio = [{'Иванов Иван': ['897097','работник']}, {'Петров Петр': ['35346', 'не раб']}]
# fio = [{1: ["Иванов", "Иван","89234145", "работник"]}]
fio = {1: {'surname': "Иванов", 'name': "Иван", 'number': "89234145", 'discrip': "работник"}}
# fio = [{'surname': "Иванов", 'name': "Иван", 'number': "89234145", 'discrip': "работник"}]

phonebook = {}
phonebook_last_id = 0


def create(db: dict, id: int, surname: str, name: str, phone: str, discrip: str) -> tuple:  # data_base
    db[id] = {"surname": surname, 'name': name, 'phone': phone, 'discrip': discrip}
    id += 1
    return db, id


def read(surname_filter: str) -> int:
    raise NotImplementedError


def get_user_data() -> tuple:
    surname = input("Введите фамилию > ")
    name = input("Введите имя > ")
    phone = input("Введите номер > ")
    discrip = input("Введите описание > ")
    return surname, name, phone, discrip


def print_data(db: dict) -> None:
    for id, data in db.items():
        print(f"[{id}: {data['surname']} | {data['name']} | {data['phone']} | {data['discrip']} ]")


def menu(db: dict, last_id: int) -> None:
    while True:
        print("Возможные действия")
        print("1. Создать запись")
        print("2. Вывести имеющиеся данные")
        print("3. Выход")
        user_input = input("Введите действие > ")
        if user_input == "1":
            record = get_user_data()
            db, last_id = create(db, last_id, *record)
        elif user_input == "2":
            print_data(db)
        elif user_input == "3":
            break


menu(phonebook, phonebook_last_id)
