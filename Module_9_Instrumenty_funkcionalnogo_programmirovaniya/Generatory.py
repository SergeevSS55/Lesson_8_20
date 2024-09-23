# Создание простого генератора
# def get_generator(n):
#     i = 0
#     while i != n:
#         yield i
#         i += 1
#
#
# obj = get_generator(20)
# print(obj)
#
# for i in obj:
#     print(i)


# Создание ф-ии Фебаначче

# def fiboracci_v1(n):
#     res = []
#     a, b = 0, 1
#     for _ in range(n):
#         res.append(a)
#         a, b = b, a + b
#     return res
#
# def fiboracci_v2(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b
#
# '''fib_1 = fiboracci_v1(n=10)
# print(fib_1)
#
# for value in fib_1:
#     print(value)'''
#
# fib_2 = fiboracci_v2(n=10)
#
# for value in fib_2:
#     print(value)
#
# for i in fib_2:
#     print(i) #не будет повторно выводиться


# #можно сделать бесконечный "список" значений
# def fiboracci_v3():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
# for value in fiboracci_v3():
#     print(value)
#     if value > 10 ** 6:
#         break


import time

start = time.time()

def read_large_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()

for line in read_large_file('large_file.txt.txt'):
    print(line)

fin = time.time()
print((fin - start) * 1000)