menu = ["first_name", "last_name", "number"]
collect = {}
d = 1

with open("phonebook.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.replace("\n", "")
        collect[d] = list(line.split(";"))
        d += 1

def findNumber(data):
    find = input("Введите запрос для поиска: ")
    for i in data:
        for j in range(len(data[i])):
            if find in data[i][j]:
                print(data[i])

def getPhone(data):
    for i in data:
        print(data[i])

def addPhone(data):
    s = 1
    save = input("Введите Ф.И. и телефон через пробел: ").split()
    while True:
        if s in data:
            s += 1
        else:
            data[s] = save
            break

def updatePhone(data):
    name = input("Введите имя или фамилию для обновления: ")
    for i in data:
        if name in data[i]:
            new_data = input("Введите новые данные через пробел: ").split()
            data[i] = new_data

def deletePhone(data):
    name = input("Введите имя или фамилию для удаления: ")
    for i in data:
        if name in data[i]:
            del data[i]

def choice(n, data):
    if n == 1:
        getPhone(data)
    elif n == 2:
        findNumber(data)
    elif n == 3:
        addPhone(data)
    elif n == 4:
        updatePhone(data)
    elif n == 5:
        deletePhone(data)

print("Выберите действие с телефонным справочником от 1 до 5:")
print("1 - показать справочник, 2 - произвести поиск по запросу, 3 - добавить данные в справочник")
print("4 - изменить данные в справочнике, 5 - удалить данные из справочника")
n = int(input())
choice(n, collect)

with open("phonebook.txt", "w", encoding="utf-8") as file:
    for k in collect:
        file.write(f"{collect[k][0]};{collect[k][1]};{collect[k][2]}\n")

print(collect)