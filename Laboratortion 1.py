import random
import csv
table = []           # вводим массив, в который запишем основную информацию о книгах
with open("books.csv", encoding='cp1251') as csvfile:
    file = csv.reader(csvfile, delimiter = ";")  # считываем файл
    cnt_zap = 0      # вводим счетчик  всех записей
    cnt_more30 = 0   # вводим счетчик записей с названием длинее 30 символов
    tegs = []        # вводим массив тегов
    fio = input("Введите ФИО автора ")  # просим ввести ФИО автора, книги которого хотим вывести
    knigi_autora = []                   # вводим массив книг автора
    max_pop = 0      # вводим переменную, в которой будем считать максимальную популярность
    for stroka in file:                 # проходимся по всем строкам файла
        if stroka[0] == "ID":           # первую строку надо пропусить, тк в ней не содержится информации о книгах
            continue
        # 1 punkt
        cnt_zap += 1
        # 2 punkt
        if len(stroka[1]) > 30:         # считаем записи, у которых в названии больше 30 символов
            cnt_more30 += 1
        # 3 punkt
        if stroka[4] == fio and int(stroka[6][6:11]) < 2016:    # записываем в массив книги выбранного автора
            knigi_autora += stroka[1] + ", "
        table.append(stroka[4] + ". " + stroka[1] + " - " + stroka[6][6:11] + '\n')  #записываем основную информацию о книгах
        # dopzadanie 1
        tegs_mestn = list(stroka[-1].split("#"))                # создаем массив "местных" тегов
        for j in tegs_mestn:                                    # если местный тег не встречался ранее, то добавляем его в массив тегов
            if j not in tegs:
                tegs.append(j)
        # dopzadanie 2 chast 1
        if int(stroka[8]) > max_pop:                            # находим наибольшую популярность
            max_pop = int(stroka[8])
    print(f"Всего в файле {cnt_zap} строк:)")
    print(f"В файле {cnt_more30} записей с названиями более 30 символов")
    print(fio, " написал(-а) : ", *knigi_autora[:-2], sep='')
    print("Все теги: ", *tegs)
# 4 punkt
f = open('resultat.txt', 'w')                                   # создаем файл, в который запишем результат работы 4 пункта
for i in range(1, 21):                                          # заполняем файл рандомными записями
    x = random.randint(0, cnt_zap)
    str_f = str(i) + ') ' + table[x]
    f.write(str_f)
f.close
# dopzadanie 2
with open("books.csv", encoding='cp1251') as csvfile:
    file = csv.reader(csvfile, delimiter = ";")                 # считываем файл
    cnt = 0
    for stroka in file:                                         # проходимся по всем строкам файла
        if stroka[0] == "ID":                                   # пропускаем первую строку файла
            continue
        if int(stroka[8]) == max_pop:
            cnt += 1
            print(f"{cnt})  {stroka[4]} -  {stroka[1]}")        # выводим книги с наибольшей популярностью до тех пор, пока их ене станет 20
        if cnt >= 20:
            break

