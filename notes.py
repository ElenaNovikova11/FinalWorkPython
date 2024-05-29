import os.path

FILE_NAME = 'note.csv'
ID = 'ID'
TITLE = 'Заголовок заметки'
NOTE = 'Сообщение заметки'
DATE = 'Дата заметки'
HEADERS = [ID, TITLE, NOTE, DATE]
ANSWER = {'y', 'yes,' 'да'}

#загрузка, если файла нет, то программа его создаст
def load_directory():
    download_file = os.path.exists('note.csv')
    date = []
    if(download_file):
        with open(FILE_NAME, 'r', encoding = 'utf-8') as file:
            for i, line in enumerate(file, start = 1):
                row = [i] + line.strip().split(";")
                date.append(dict(zip(HEADERS, row)))

        return date

    else:
        file = open(FILE_NAME, 'a+', encoding = 'utf-8')
        file.close()
        print("\n\tСоздался файл для заметок")
        return date


#вывод всех заметок на экран
def print_note(date):
    for item in date:
        print(*(f"{k}: {v:<16}" for k, v in item.items()))

#вывод заметки по дате
def print_date(date):
    date_user = input('Введите дату, для вывода конкретной заметки: ')
    date_user.strip().capitalize()
    for item in date:
        if item[DATE] == date_user:
            print(*(f"{k}: {v:<16}" for k, v in item.items()))
        else:
            print("На эту дату нет заметки")


#добавление новой заметки и сохранение
def add_new_note(date):
    row = input('Введите заголовок заметки, сообщение заметки, дату создания, разделяя(;): ').split(";")
    line = [len(date) + 1] + [item.strip().capitalize() for item in row]
    date.append(dict(zip(HEADERS, line)))
    print("Добавлена новая заметка")

    with open(FILE_NAME, 'a+', encoding = 'utf-8') as file:
        file.write('; '.join(f"{v}" for k, v in date[len(date) - 1].items() if k != ID) + "\n")
        print("Файл обновлен и в него добавлена новая заметка")

#изменение заметки
def edit_text_note(title_old: str, date):
    new_note = input("Введите новый текст заметки: ")
    new_note.strip().capitalize()
    for item in date:
        if item[TITLE] == title_old:
            item[NOTE] = new_note
            print("Изменения сохранены")
            print(*(f"{k}: {v:<16}" for k, v in item.items()))

            with open(FILE_NAME, 'w', encoding='utf-8') as file:
                for note in date:
                    for k, v in note.items():
                        if k != ID:
                            file.write(f"{v}; ")
                    file.write("\n")
                print("Данные в фале изменены")

    # Выводим все строки после изменения
  #  for note in date:
  
  #      print(*(f"{k}: {v:<16}" for k, v in note.items()))


#удаление по конкретному ID
def delete_id(number: str, date):
    id_num = int(number)

    if number.isdigit() and id_num <= len(date):
        print(*(f"{k}: {v:<16}" for k, v in date[len(date) - 1].items()))
        delete_n = input("Удаляем (y/n): ")
        if delete_n in {'y', 'yes', 'да'}:
            date.pop(id_num - 1)
            print("Запись успешно удалена")

            with open(FILE_NAME, 'w', encoding='utf-8') as file:
                for note in date:
                    for k, v in note.items():
                        if k != ID:
                            file.write(f"{v}; ")
                    file.write("\n")
                print("Файл обновлен")
        else:
            print(f"Записи под номером - {ID} нет.")

        # Выводим все строки после удаления
       # for note in date:
        #    print(*(f"{k}: {v:<16}" for k, v in note.items()))

#вывод методов на экран
def main(date):
    while (True):
        print(f'''\nЧто вы хотите сделать?
        1: Вывести на экран все заметки
        2: Добавить и сохранить новую заметку
        3: Редактировать заметку по названию заметки
        4: Вывести на экран заметку по определенной дате
        5: Удалить заметку
        0: Выйти''')

        x = input('Ваш выбор: ')

        if x == "1":
            print_note(date)
        elif x == "2":
            add_new_note(date)   
        elif x == "3":
            title_old = input("Введите заголовок заметки, которую хотите заменить: ")
            title_old.strip().capitalize()
            edit_text_note(title_old= title_old, date=date)
        elif x  == "4":
            print_date(date)
        elif x == "5":
            num_cell = input("Введите ID которое хотите удалить: ")
            delete_id(number = num_cell, date = date)
        elif x == "0":
            break
        else:
            print("Неверная команда")

if __name__ == '__main__':
    main(load_directory())