from GA_pyeasyga import GApyeasyga
from GA_MyAlg import GeneticAlgorithm
import json
import requests

# список, содержащий кортежи с данными
data = []
MaxWeight, MaxVolume = 0, 0


def main():
    # читаем файлик
    with open('37.txt') as file_handler:
        lst = file_handler.readlines()
        pos = lst[0].find(' ')
        # получаем макс. грузоподъемность и макс. вместимость
        global MaxWeight, MaxVolume
        MaxWeight, MaxVolume = int(lst[0][:pos]), int(lst[0][pos + 1:])
        # получаем кортежи с информацией, начиная со 2 строки файла
        for i in range(1, len(lst)):
            # вытаскиваем цифры
            t = lst[i].replace('\n', '').split(' ')
            # составляем входные данные
            data.append((int(t[0]), float(t[1]), int(t[2])))

# ЗАДАНИЕ 1
# ---------------------------
# формирование ответа
    ansTask1 = Task1()
    print("Task#1")
    print(ansTask1)
# ---------------------------
# ЗАДАНИЕ 2
# ---------------------------
    ansTask2 = Task2()
    print("Task#2")
    print(ansTask2)
# составление json ответа
    js=json.dumps({"1":ansTask1,"2":ansTask2},indent=6)
    print(js)
    r = requests.post('https://cit-home1.herokuapp.com/api/ga_homework', js,
                      headers={'Content-type': "application/json"})
    # смотрим АШШШШИБК!!! или извещение об успехе
    print(r.json())
# ---------------------------

def Task1():
    # инициализируем алгоритм
    GA=GApyeasyga(data, MaxWeight, MaxVolume)
    # прогон 20 раз, запись в файл для визуальной проверки
    temp = []
    for i in range(0, 20):
        obj = GA.solve()
        temp.append(obj)
    return parse(temp)


def Task2():
    # прогон 20 раз, запись в файл для визуальной проверки
    temp = []
    for i in range(0, 20):
        # создали объект с начальной популяцией
        ga = GeneticAlgorithm(data, MaxWeight, MaxVolume, 200)
        # отбор особей для скрещивания,получение нового поколения, отбор 200 лучших в новую популяцию
        #100 поколений
        for i in range(0, 100):
            ga.nextPop()
            newBest = ga.bestInd()
        temp.append(newBest)
    return Newparse(temp)

def Newparse(temp):
    # запись в файл
    DataSet37=[]
    with open('AnsPyeasyga.txt', 'a') as wr:
        wr.write("Task #2" + '\n')
        for obj in temp:
            #переводим бинарный вектор в номера предметов
            items=[]
            for i,bit in enumerate(obj.cort):
                if bit==1:
                    items.append(i+1)
            wr.write(str({"value": obj.price, "weight": obj.weight, "volume": round(obj.volume), "items": items}) + '\n')
            DataSet37.append({"value": obj.price, "weight": obj.weight, "volume": round(obj.volume), "items": items})
        # сортируем, выбирая лучший результат
        DataSet37.sort(key=lambda d: d["value"], reverse=True)
        wr.write("Best: " + str(DataSet37[0]) + '\n')
    return DataSet37[0]

# составляем датасет, из него берем макс
def parse(temp):
    # запись в файл
    DataSet37 = []
    with open('AnsPyeasyga.txt', 'a') as wr:
        wr.write("Task #1" + '\n')
        for obj in temp:
            weight = 0
            volume = 0
            items = []
            for i, item in enumerate(obj[1]):  # смотрим, какие элементы входят и считаем объем и вес
                if item == 1:
                    weight += data[i][0]
                    volume += data[i][1]
                    items.append(i + 1)
            volume = round(volume)  # округляем до целых
            wr.write(str({"value": obj[0], "weight": weight, "volume": volume, "items": items}) + '\n')
            DataSet37.append({"value": obj[0], "weight": weight, "volume": volume, "items": items})
        # сортируем
        DataSet37.sort(key=lambda d: d["value"], reverse=True)
        wr.write("Best: " + str(DataSet37[0]) + '\n')
    return DataSet37[0]


if __name__ == "__main__":
    main()
