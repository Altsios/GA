# GA
Решение для варианта №37
## Запуск
* используется функция main() в ней:
  * Чтение файла 37.txt для получения данных
  ```python
  with open('37.txt') as file_handler:
  ```
  * Вызов Task#1 и Task#2
  * Формирование и отправка ответа
## Задание №1
* Используется библиотека pyeasyga.py. Начальная популяция –кол-во особей всегда = 200
* Реализован вспомогательный класс GApyeasyga.
```python
class GApyeasyga:
    def __init__(self,data,W,V):
        # инициализируем алгоритм данными
        self.ga=pyeasyga.GeneticAlgorithm(data)
        # устанавливаем популяцию равной 200
        self.ga.population_size = 200
        self.ga.fitness_function = self.fitness  # установка фитнес-функции
        self.MaxWeight=W
        self.MaxVolume=V
```
* Алгоритм запускается 20 раз, после чего выбирается лучший ответ
```python
for i in range(0, 20)
```
## Задание №2
Созданы 2 класса:
* Сущность
```python
    class Individ:
    def __init__(self, cntW, cntV, cntP, cort):
        self.weight = cntW
        self.volume = cntV
        self.price = cntP
        self.cort = cort
        self.fitness = 0
 ```
* Алгоритм
 ```python
    class GeneticAlgorithm:
    def __init__(self, data, W, V, cnt):
        self.data = data
        self.MaxWeight = W
        self.MaxVolume = V
        self.cnt = cnt  # количество особей в популяции
        # на первом шаге еще нет следующего поколения
        self.current_generation = self.createStartPop()
        self.next_generation = []
  ```
Согласно распределению операторов:
* Начальная популяция –кол-во особей всегда = 200.
  ```python
    ga = GeneticAlgorithm(data, MaxWeight, MaxVolume, 200)
  ```
  * Жадный выбор, начиная со случайного груза
  ```python
    def createStartPop(self)
  ```
* Отборособей для скрещивания
  * Выбор каждой особи пропорционально приспособленности (рулетка)
  ```python
    def roulette(self, tmpPar, pars)
  ```
* Скрещивание (кроссинговер) между выбранными особями. Каждая особь скрещивается 1 раз за 1 поколение, 1 пара дает 2 потомка:
  * Однородный (каждый бит от случайно выбранного родителя)
  ```python
    def crossing(self, mother, father)
  ```
* Мутация
  * Инвертирование всех битов у 1 особи
  ```python
    def mutation(self,data)
  ```
* Формирование новой популяции (кол-во особей -константа)
  * «штраф» за «старость» -20% функции приспособленности, выбор лучших
  ```python
    for old in self.current_generation:
       old.fitness *= 0.8
  ```
* Оценка результата
  * Прошло 100 покоелений
 * Алгоритм запускается 20 раз, после чего выбирается лучший ответ
 ```python
for i in range(0, 20)
```
## Форма ответа
* В ответе нумерация особей ведется с 1, т.е. 1я особь имеет номер 1, 30я-30.
  * вектор [1,0,1,1] интерпретируется как предметы [1,3,4]  
* Запись результатов осуществляется в файл AnsPyeasyga.txt
