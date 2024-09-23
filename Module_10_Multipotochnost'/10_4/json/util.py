import json
import datetime
from random import randint

res = []
files = ['file1.json', 'file2.json', 'file3.json', 'file4.json']

# for file in files: #пополнение файлов json списками из чисел
#     for _ in range(1000):
#         res.append(randint(0, 1000)) #res.append(str(randint(0, 30))) изменение на строки
#     with open(file, 'w') as f:
#         json.dump(res, f)
#     res = []

res_to_count = []
start = datetime.datetime.now()

for file in files:
    with open(file, 'r') as f:  # открываем файлы по очереди
        data = json.load(f)  # загружаем из определенного файла в переменную дата один из списков
        res_to_count.extend(data)  # объединение списков в один из всех элементов дата
print(sum(res_to_count))
end = datetime.datetime.now()
print(end - start)
