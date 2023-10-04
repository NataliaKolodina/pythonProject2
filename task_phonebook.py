import os, re


def printData(data):
    phoneBook = []
    print(" ")
    print(" №  Фамилия          Имя          Телефонный номер")
    print(" ")
    personID = 1
    for contact in data:
        lastName, name, phone = contact.rstrip().split(",")
        phoneBook.append(
            {
                "ID": personID,
                "lastName": lastName,
                "name": name,
                "phone": phone,
            }
        )
        personID += 1
    for contact in phoneBook:
        personID, lastName, name, phone = contact.values()
        print(f"{personID:>2}. {lastName:<15} {name:<10} -- {phone:<15}")
    print(" ")


def showCont(fileName):
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
    return


def addCont(fileName):
    os.system("cls")
    with open(fileName, "a", encoding="UTF-8") as file:
        res = ""
        res += input("Введите фамилию: ") + ","
        res += input("Введите имя: ") + ","
        res += input("Введите телефонный номер: ")
        file.write(res + "\n")
    input("\nКонтакт был добавлен!")
    return


def findCont(fileName):  # Функция поиска контактов в телефонной книге
    os.system("cls")
    target = input("Введите Фамилию, Имя или номер телефона контакта для поиска: ")
    result = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if target in person:
                result.append(person)
    if len(result) != 0:
        printData(result)
    else:
        print(f"Нужный контакт: '{target}' в справочнике отсутствует.")
    return


def changeCont(fileName):
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
        numberCont = int(
            input("Введите номер контакта, который Вы хотите изменить, или 0 для выхода: ")
        )
        print(data[numberCont - 1].rstrip().split(","))
        if numberCont != 0:
            newLastName = input("Введите новую фамилию: ")
            newName = input("Введите новое имя: ")
            newPhone = input("Введите новый номер телефона: ")
            data[numberCont - 1] = (
                    newLastName + "," + newName + "," + newPhone + "\n"
            )
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nКонтакт был изменен!")
                return
        else:
            return


def deleteCont(fileName):
    os.system("cls")
    with open(fileName, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
        numberCont = int(
            input("Введите номер контакта, который Вы хотите удалть или 0 для выхода: ")
        )
        if numberCont != 0:
            print(f"Удаление записи: {data[numberCont - 1].rstrip().split(',')}\n")
            data.pop(numberCont - 1)
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
        else:
            return
    return


def menu():
    print("* Меню телефонного справочника *")
    print(" ")
    print(" [1] -- Показать все контакты")
    print(" [2] -- Добавить контакт")
    print(" [3] -- Найти контакт")
    print(" [4] -- Изменить контакт")
    print(" [5] -- Удалить контакт")
    print("\n [0] -- Выход")


def main(file_name):
    while True:
        os.system("cls")
        menu()
        userChoice = int(input("Введите номер от 1 до 5 или 0 для выхода: "))
        if userChoice == 1:
            showCont(file_name)
        elif userChoice == 2:
            addCont(file_name)
        elif userChoice == 3:
            findCont(file_name)
        elif userChoice == 4:
            changeCont(file_name)
        elif userChoice == 5:
            deleteCont(file_name)
        elif userChoice == 0:
            print("Работа окончена!")
            return


path = "phonebook.txt"
main(path)
