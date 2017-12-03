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
* Используется библиотека pyeasyga.py. 
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
## Задание №2
*
* Алгоритм запускается 20 раз, после чего выбирается лучший ответ
## Форма ответа
* В ответе нумерация особей ведется с 1, т.е. 1я особь имеет номер 1, 30я-30.
  * вектор [1,0,1,1] интерпретируется как предметы [1,3,4]  
* Запись результатов осуществляется в файл AnsPyeasyga.txt
