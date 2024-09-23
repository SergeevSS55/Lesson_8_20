import time
import threading
import sys


def excepthook2(args, a, b):
    print('handeled')


sys.excepthook = excepthook2


def some_func():
    time.sleep(4)
    raise Exception


def excepthook(args):
    print(args.thread.name)
    print(args.thread.is_alive())


threading.excepthook = excepthook

t1 = threading.Thread(target=some_func)
t2 = threading.Thread(target=some_func)

t1.start()
t2.start()

t1.join()
t2.join()

raise Exception # для exceptionhook из sys
