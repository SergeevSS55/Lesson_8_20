import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()


def thread_task1():
    lock_1.acquire()
    print('thread 1 lock_1 acquire')
    time.sleep(1)
    lock_2.acquire()
    print('thread 1 lock_2 acquire')
    lock_2.release()
    lock_1.release()


def thread_task2():
    lock_2.acquire()
    print('thread 2 lock_2 acquire')
    time.sleep(1)
    lock_1.acquire()
    print('thread 2 lock_1 acquire')
    lock_1.release()
    lock_2.release()


t1 = threading.Thread(target=thread_task1)
t2 = threading.Thread(target=thread_task2)

t1.start()
t2.start()

t1.join()
t2.join()
