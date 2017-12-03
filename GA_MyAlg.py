import random


class Individ:
    def __init__(self, cntW, cntV, cntP, cort):
        self.weight = cntW
        self.volume = cntV
        self.price = cntP
        self.cort = cort
        self.fitness = 0

    # фитнес-функция
    def findFitness(self, MaxWeight, MaxVolume):
        # если не проходим по ограничению, особь не жизнеспособна
        if self.weight > MaxWeight or self.volume > MaxVolume:
            self.fitness = 0
        else:  # иначе определяем ее "приспособленность" как ценность
            self.fitness = self.price

    def mutation(self,data):
        for i in range(0, len(self.cort)):
            # пересчет характеристик после мутации сразу
            if self.cort[i] == 1:
                self.cort[i] = 0
                self.weight-=data[i][0]
                self.volume-= data[i][1]
                self.price -= data[i][2]
            else:
                self.cort[i] = 1
                self.weight += data[i][0]
                self.volume += data[i][1]
                self.price += data[i][2]


class GeneticAlgorithm:
    def __init__(self, data, W, V, cnt):
        self.data = data
        self.MaxWeight = W
        self.MaxVolume = V
        self.cnt = cnt  # количество особей в популяции
        # на первом шаге еще нет следующего поколения
        self.current_generation = self.createStartPop()
        self.next_generation = []

    # создание следующей популяции
    def nextPop(self):
        # получили следующее поколение
        self.next_gen()
        # у старого поколения забираем 20% функции приспособленности(оставляем 80%)
        for old in self.current_generation:
            old.fitness *= 0.8
        # у нового поколения рассчитываем приспособленность
        for new in self.next_generation:
            new.findFitness(self.MaxWeight,self.MaxVolume)
        # отбираем 200 лучших из двух поколений
        newPop=self.current_generation.copy()
        for new in self.next_generation:
            newPop.append(new)
        newPop.sort(key=lambda i: i.fitness, reverse=True)
        newPop = newPop[:self.cnt]
        # теперь это текущее поколение
        self.current_generation=newPop
        self.next_generation=[]

    def bestInd(self):
        return (self.current_generation[0])
    # генерация следующего поколения
    def next_gen(self):
        tmpPar = self.current_generation.copy()
        # pars содержит кортежи-пары
        pars = []
        # выбор пары по рулетке
        self.roulette(tmpPar, pars)
        # кроссинговер
        for par in pars:
            self.crossing(par[0], par[1])
        # проводим мутацию, выбирая случайную особь
        choice = random.randint(0, self.cnt - 1)
        self.next_generation[choice].mutation(self.data)

    def crossing(self, mother, father):
        # кортежи
        fstCh = []
        secCh = []
        # сразу подсчитываем характеристики
        cntW1 = 0
        cntV1 = 0
        cntP1 = 0
        cntW2 = 0
        cntV2 = 0
        cntP2 = 0
        # однородный кроссинговер
        for i in range(0, len(self.data)):
            if mother.cort[i] == father.cort[i]:
                fstCh.append(mother.cort[i])
                secCh.append(mother.cort[i])
                if mother.cort[i] == 1:
                    cntW1 += self.data[i][0]
                    cntV1 += self.data[i][1]
                    cntP1 += self.data[i][2]
                    cntW2 += self.data[i][0]
                    cntV2 += self.data[i][1]
                    cntP2 += self.data[i][2]
            else:
                num = random.randint(0, 1)
                fstCh.append(num)
                if num == 1:
                    cntW1 += self.data[i][0]
                    cntV1 += self.data[i][1]
                    cntP1 += self.data[i][2]
                num = random.randint(0, 1)
                secCh.append(num)
                if num == 1:
                    cntW2 += self.data[i][0]
                    cntV2 += self.data[i][1]
                    cntP2 += self.data[i][2]

        # составляем след поколение
        self.next_generation.append(Individ(cntW1, cntV1, cntP1, fstCh))
        self.next_generation.append(Individ(cntW2, cntV2, cntP2, secCh))

    # создание отрезка и выбор двух особей
    def roulette(self, tmpPar, pars):
        mother = None
        father = None
        # пока явно не останется 1 пара в популяции
        while len(tmpPar) > 2:
            # создание "отрезка"
            # n-число подотрезков
            line = []
            n = len(tmpPar)
            start, end = 0, 0
            for i in range(0, n):
                start = end + 0.000000000001  # +, чтобы конец и начало пред различались
                # просто складываем значения, формируя отрезок
                end += tmpPar[i].fitness
                line.append((start, end))
            # случайное число
            dart = random.uniform(0.0000000000011, end)
            # формируем пару
            for i, subline in enumerate(line):
                if dart >= subline[0] and dart <= subline[1]:
                    # попали? берем в пару, убирая из списка
                    if not mother:
                        mother = tmpPar[i]
                        tmpPar.remove(mother)
                        break
                    else:
                        father = tmpPar[i]
                        tmpPar.remove(father)
                        break
            if mother and father:
                pars.append((mother, father))
                mother = None
                father = None
        # добавляем оставшихся 2х
        pars.append((tmpPar[0], tmpPar[1]))

    # начиная с start по end(искл) заполняем вектор особи
    def put(self, indiv, tmp, start, end, cntW, cntV, cntP):
        for i in range(start, end):
            # проверяем, прежде чем произвести вставку
            if cntW + tmp[i][0] <= self.MaxWeight and cntV + tmp[i][1] <= self.MaxVolume:
                cntW += tmp[i][0]
                cntV += tmp[i][1]
                cntP += tmp[i][2]
                indiv[i] = 1  # мы добавили особь в популяцию
        return cntW, cntV, cntP

    # создание начальной популяции(жадный выбор, начиная со случайного груза)
    def createStartPop(self):
        # список с получившейся популяцией, изначально все позиции пусты
        pop = []
        tmp = self.data.copy()
        # сортировка по убыванию ценности
        tmp.sort(key=lambda i: i[2], reverse=True)
        # жадный выбор(cnt особей)
        for i in range(0, self.cnt):
            # особь, изначально все позиции пусты
            indiv = [0 for i in range(0, 30)]
            # добавляем, пока позволяют грузопод. и объем
            # случайная позиция
            pos = random.randint(0, 29)
            # ограничители
            cntW = 0
            cntV = 0
            # храним ценность заодно
            cntP = 0
            # начинаем со случайной позиции
            cntW, cntV, cntP = self.put(indiv, tmp, pos, len(tmp), cntW, cntV, cntP)
            # если мы все просмотрели, но можно еще впихнуть,
            # идем от начала до случайной позиции, занося оставшихся, пока это возможно
            if cntW < self.MaxWeight and cntV < self.MaxVolume:
                cntW, cntV, cntP = self.put(indiv, tmp, 0, pos, cntW, cntV, cntP)
            # формирование популяции
            pop.append(Individ(cntW, cntV, cntP, indiv))
        for indiv in pop:
            # для каждого вычисляется фитнесс функция
            indiv.findFitness(self.MaxWeight, self.MaxVolume)
        pop.sort(key=lambda i: i.fitness, reverse=True)
        return pop
