# # Пример 1 - библиотека iertools
# from itertools import repeat
# import sys
#
# ex_iterator = repeat('4', 100_100)
# print(ex_iterator)
# print(f'размер итератора - {sys.getsizeof(ex_iterator)}')
#
# ex_str = '4' * 100_100
# print(f'размер списка - {sys.getsizeof(ex_str)}')


# class Iter:
#     def __init__(self):
#         self.first = 'Первый элемент'
#         self.second = 'Второй элемент'
#         self.third = 'Третий элемент'
#         self.i = 0
#
#     def __iter__(self):
#         # обнуляем счетчик перед циклом
#         self.i = 0
#         # возвращаем ссылку на себя, так как сам объект должен быть итератором
#         return self
#
#     def __next__(self):
#         # этот метод возвращает значения по требованию питона (ленивые вычисления)
#         self.i += 1
#         if self.i == 1:
#             return self.first
#         if self.i == 2:
#             return self.second
#         if self.i == 3:
#             return self.third
#         if self.i == 4:
#             return 'Подсчет окончен'
#         raise StopIteration() # признак того, что возвращать больше нечего
#
# obj = Iter()
# print(obj)
#
# for value in obj:
#     print(value)
# #
# # Т.е. интерпритатор вызывает метод некст при каждом проходе цикла
# # Если в некст возникает исключение СтопИтэрэйшен, то значит в объекте нет больше элементов, цикл прекращается


# # пример 3 - что происходит с циклом ФОР по итератору
# class Iter:
#     def __init__(self):
#         self.first = 'Первый элемент'
#         self.second = 'Второй элемент'
#         self.third = 'Третий элемент'
#         self.i = 0
#
#     def __iter__(self):
#         # обнуляем счетчик перед циклом
#         self.i = 0
#         # возвращаем ссылку на себя, так как сам объект должен быть итератором
#         return self
#
#     def __next__(self):
#         # этот метод возвращает значения по требованию питона (ленивые вычисления)
#         self.i += 1
#         if self.i == 1:
#             return self.first
#         if self.i == 2:
#             return self.second
#         if self.i == 3:
#             return self.third
#         if self.i == 4:
#             return 'Подсчет окончен'
#         raise StopIteration() # признак того, что возвращать больше нечего
#
# obj = Iter()
#
# try:
#     while True:
#         value = obj.__next__()
#         print(value)
# except StopIteration:
#     pass


# def fiboracci(n):
#     res = []
#     a, b = 0, 1
#     for _ in range(n):
#         res.append(a)
#         a, b = b, a + b
#     return res
#
# for value in fiboracci(n=10):
#     print(value)

# Тоже самое, но на примере собственного итерратора
class Febanacci:
    # Итератор последовательности  Фебоначчи до N Элементов
    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0, 0, 1, n

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a


fib_iteration = Febanacci(20)
print(fib_iteration)
for value in fib_iteration:
    print(value)
