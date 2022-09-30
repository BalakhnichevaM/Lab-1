import random
import csv
table = []
with open("books.csv", encoding='cp1251') as csvfile:
    file = csv.reader(csvfile, delimiter = ";")
    cnt_zap = 0
    cnt_more30 = 0
    tegs = []
    fio = input("Введите ФИО автора ")
    knigi_autora = []
    max_pop = 0
    for stroka in file:
        if stroka[0] == "ID":
            continue
        # 1 punkt
        cnt_zap += 1
        # 2 punkt
        if len(stroka[1]) > 30:
            cnt_more30 += 1
        # 3 punkt
        if stroka[4] == fio and int(stroka[6][6:11]) < 2016:
            knigi_autora += stroka[1] + ", "
        table.append(stroka[4] + ". " + stroka[1] + " - " + stroka[6][6:11] + '\n')
        # dopzadanie 1
        tegs_mestn = list(stroka[-1].split("#"))
        for j in tegs_mestn:
            if j not in tegs:
                tegs.append(j)
        # dopzadanie 2 chast 1
        if int(stroka[8]) > max_pop:
            max_pop = int(stroka[8])
    print(f"Всего в файле {cnt_zap} строк:)")
    print(f"В файле {cnt_more30} записей с названиями более 30 символов")
    print(fio, " написал(-а) : ", *knigi_autora[:-2], sep='')
    print("Все теги: ", *tegs)
# 4 punkt
f = open('resultat.txt', 'w')
for i in range(1, 21):
    x = random.randint(0, cnt_zap)
    str_f = str(i) + ') ' + table[x]
    f.write(str_f)
f.close
# dopzadanie 2
with open("books.csv", encoding='cp1251') as csvfile:
    file = csv.reader(csvfile, delimiter = ";")
    cnt = 0
    for stroka in file:
        if stroka[0] == "ID":
            continue
        if int(stroka[8]) == max_pop:
            cnt += 1
            print(f"{cnt})  {stroka[4]} -  {stroka[1]}")
        if cnt >= 20:
            break

