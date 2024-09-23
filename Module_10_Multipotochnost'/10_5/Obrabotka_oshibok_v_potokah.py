import threading
import time


def some_func():
    time.sleep(4)
    raise Exception


def thread_func():
    try:
        some_func()
    except Exception as e:
        print(f'Wow! Exception - {type(e)}') #  можно указать вместо принта - pass


t1 = threading.Thread(target=thread_func)
t2 = threading.Thread(target=thread_func)

t1.start()
t2.start()

t1.join()
t2.join()
