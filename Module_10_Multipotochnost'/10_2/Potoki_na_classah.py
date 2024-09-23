from threading import Thread
import requests


class Getter(Thread):
    res = []  # каждый поток складывает в этот список найденный по ЮРЛ жанру

    def __init__(self, URL):
        self.The_URL = URL
        super().__init__() #thread.__init__() not called если не указать
    def run(self):
        response = requests.get(self.The_URL)
        Getter.res.append(response.json())


threads = []
num_of_genres = 10
for i in range(num_of_genres):
    thread = Getter('https://binaryjazz.us/wp-json/genrenator/v1/genre/')  # поток инициализируется от класса Геттер
    thread.start()  # метод старт вызывает метод(функцию в классе) ран
    threads.append(thread)  # экземпляр класса Геттер кладется в трэдс (список),
    # чтоб впоследствии смогли вызвать метод джойн

for thread in threads:
    thread.join()

print(Getter.res)
assert len(Getter.res) == num_of_genres #если длина не будет соответствовать заданным нами количеством жанров,
# то вызовется ошибка АсашенЭрор
