from data_create import name_data, surname_data, phone_data, address_data

def remove_lines(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    modified_lines = []
    for line in lines:
        if line.strip():
            modified_lines.append(line)

    with open(file_name, "w") as file:
        for line in modified_lines:
            file.write(line)
def edit_data():
    remove_lines("data_first_variant.csv")
    remove_lines("data_second_variant.csv")
    choice = int(input("Выберите вариант: \n1 - Изменить данные в первом файле\n2 - Изменить данные во втором файле\n"))
    while choice != 1 and choice != 2:
        print("Неправильный ввод")
        choice = int(input("Выберите вариант: \n1 - Изменить данные в первом файле\n2 - Изменить данные во втором файле\n"))

    if choice == 1:
        with open("data_first_variant.csv",'r',encoding='utf-8') as f:
            data = f.readlines()
        print("Доступные данные для изменения:")
        print(*data)

        number_line = int(input("Введите номер строки для изменения:  "))
        while number_line < 1 or number_line > len(data):
            print("Неправильный номер строки")
            number_line = int(input("Введите номер строки для изменения:  "))

        new_data = input("Введите новые данные:  ")

        data[number_line-1] = new_data + "\n"

        with open ("data_first_variant.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print("Изменения сохранены")    

    elif choice == 2:
            with open("data_second_variant.csv",'r',encoding='utf-8') as f:
                data = f.readlines()
            print("Доступные данные для изменения:")
            print(*data)

            number_line = int(input("Введите номер строки для изменения:  "))
            while number_line < 1 or number_line > len(data):
                print("Неправильный номер строки")
            number_line = int(input("Введите номер строки для изменения:  "))

            new_data = name_data() + ";" + surname_data() + ";" + phone_data() + ";" + address_data()
            data[number_line-1] = new_data + "\n"

            with open ("data_second_variant.csv", 'w', encoding='utf-8') as f:
                f.writelines(data)
            print("Изменения сохранены")

def delete_data():
    choice = int(input("Выберите вариант: \n1 - Удалить данные из первого файла\n2 - Удалить данные из второго файла\n"))
    while choice != 1 and choice != 2:
        print("Неправильный ввод")
        choice = int(input("Выберите вариант: \n1 - Удалить данные из первого файла\n2 - Удалить данные из второго файла\n"))

    if choice == 1:
        with open("data_first_variant.csv", 'r', encoding= 'utf-8') as f:
            data = f.readlines()

        print("Доступные данные для удаления")
        print(*data)

        number_line = int(input("Введите номер строки для удаления:"))
        while number_line < 1 or number_line > len(data):
            print("Неправильный номер строки")
            number_line = int(input("Введите номер строки для удаления:"))

        del data[number_line-1]

        with open("data_first_variant.csv", 'w', encoding= 'utf-8') as f:
            f.writelines(data)
        print("Данные удалены")

    elif choice == 2:
        with open("data_second_variant.csv", 'r', encoding= 'utf-8') as f:
            data = f.readlines()
        print("Доступные данные для удаления")
        print(*data)

        number_line = int(input("Введите номер строки для удаления:"))
        while number_line < 1 or number_line > len(data):
            print("Неправильный номер строки")
            number_line = int(input("Введите номер строки для удаления:"))

        del data[number_line-1]
        with open("data_second_variant.csv", 'w', encoding= 'utf-8') as f:
            f.writelines(data)
        print("Данные удалены")    


            









