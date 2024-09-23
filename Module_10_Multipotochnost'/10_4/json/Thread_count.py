import json
from threading import Thread
import datetime

res = []
threads = []
files = ['file1.json', 'file2.json', 'file3.json', 'file4.json']


def worker(file):
    with open(file, 'r') as f:
        js = json.load(f)
        res.extend(js)



start = datetime.datetime.now()

for i in range(len(files)):  # создавалось то количество потоков сколько есть файлов
    t = Thread(target=worker, args=(files[i],))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = datetime.datetime.now()


print(sum(res))
print(end - start)
