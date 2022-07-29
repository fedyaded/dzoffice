def main():
    # Учёт техники в компании, ключ это предмет в компании, значение это список["адрес","человек","id","цена"]
    # вывод информации, перемещение в другое место, перепривяку к другому человеку, удаление, добавление, редактирование
    # сделать словарь для учёта офисов
    offices={}
    exit = True
    while exit:
        choose=int(input("1.Заниматься офисами\n3.ВЫХОД\n-> "))
        if choose == 1:
            while exit:
                choose = int(input("1.ДОБАВИТЬ\n2.РЕДАКТИРОВАТЬ\n3.УДАЛИТЬ\n4.ВЫВОД ВСЕХ\n5.ВЫХОД\n-> "))
                if choose == 1:
                    f = open ("ofic.txt","w")
                    name =input("Ввести название ")
                    adres = input("Ввести адрес ")
                    offices.update({name:adres})
                    f.write(str(offices))
                    f.close ()
                elif choose == 2:
                    f = open ("ofic.txt","a")
                    name = input("Ввести название ")
                    if name in offices.keys():
                        new_adres = input("Ввести адрес ")
                        offices[name]= new_adres
                        for element in techs:
                            if techs[element][1]==name:
                                techs[element][0]=new_adres
                    else:
                        print("Нет такого офиса")
                elif choose == 3:
                    f = open("ofic.txt","r")
                    name = input("Ввести название ")
                                        if name in offices.keys():
                        offices.pop(name)

                        for element in techs:
                            if techs[element][1] == name:
                                techs.pop(element)
                    else:
                        print("Нет такого офиса")
                    f.close ()
                elif choose == 4:
                    f = open("ofic.txt","r")
                    for el in f:
                        print(el)
                elif choose == 5:
                    exit = False
                else:
                    print("Некорректный ввод, повторите попытку")
            exit = True
        elif choose == 3:
            exit = False
        else:
            print("Некорректный ввод, повторите попытку")


main()
