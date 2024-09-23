#В версиях Питона меньше 3.10 потоки не могут вывести 20_000_000, поскольку это не являлось отомарным решением
# Для решения данной проблемы существуют блокировки
# Блокировка позволяет на определенном участке кода раотать только одному потоку

# race_condition (условия гонки)

from threading import Thread, Lock

x = 0

lock = Lock() #создаем один замок. Тот котопрый закрыл - тот и открыл

def thread_task():
    global x
    for i in range(10_000_000):
        lock.acquire()
        x = x + 1
        lock.release()

def thread_task():
    global x
    for i in range(1_000_000):
        try:
            lock.acquire()
            x += 1
        finally:
            lock.release()

def main():
    global x
    x = 0

    t1 = Thread(target=thread_task)
    t2 = Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


for i in range(10):
    main()
    print(x)
