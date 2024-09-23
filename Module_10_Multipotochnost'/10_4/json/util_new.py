import json
import datetime
from random import randint

res = []
files = ['file1.json', 'file2.json', 'file3.json', 'file4.json']


def main():
    res_to_count = []
    start = datetime.datetime.now()

    for file in files:
        with open(file, 'r') as f:  # открываем файлы по очереди
            data = json.load(f)  # загружаем из определенного файла в переменную дата один из списков
            res_to_count.extend(data)  # объединение списков в один из всех элементов дата
    sum(res_to_count)
    end = datetime.datetime.now()
    return end - start


time_calc = []
for i in range(1000):
    res = []
    time_calc.append(main())
print(sum([calc.microseconds for calc in time_calc]) / len(time_calc))
