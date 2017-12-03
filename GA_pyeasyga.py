from pyeasyga import pyeasyga

class GApyeasyga:
    def __init__(self,data,W,V):
        # инициализируем алгоритм данными
        self.ga=pyeasyga.GeneticAlgorithm(data)
        # устанавливаем популяцию равной 200
        self.ga.population_size = 200
        self.ga.fitness_function = self.fitness  # установка фитнес-функции
        self.MaxWeight=W
        self.MaxVolume=V


    #  определяем фитнесс функцию согласно документации
    def fitness(self,individual, data):
        weight, volume, price = 0, 0, 0
        for (selected, item) in zip(individual, data):
            if selected:
                weight += item[0]
                volume += item[1]
                price += item[2]
        if weight > self.MaxWeight or volume > self.MaxVolume:
            price = 0
        return price

    def solve(self):
        self.ga.run()  # запуск алгоритма
        return self.ga.best_individual()
