# race_condition (условия гонки)

import threading

x = 0


def thread_task():
    global x
    for i in range(10_000_000):
        x = x + 1 #читает значение х (х = 55), вычисляет значение х (х = х + 1) и записывает следующее значение х (х = 56)


def main():
    global x
    x = 0

    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


for i in range(10):
    main()
    print(x)
