# my_func = lambda x: x + 10
# print(my_func(x=42))
# print(type(my_func))


# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# result = map(lambda x: x + 10, my_numbers)
# print(list(result))


# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
#
# res = map(lambda x, y: x + y, my_numbers, they_numbers)
# print(list(res))

#
# def get_multiplier_v1(n):
#     if n == 2:
#         def multiplier(x):
#             return x * 2
#
#     elif n == 3:
#         def multiplier(x):
#             return x * 3
#
#     else:
#         raise Exception ('Я могу умножать только на 2 или 3!')
#
#     return multiplier
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# by_2 = get_multiplier_v1(2)
# by_3 = get_multiplier_v1(3)
#
# result = map(by_2, my_numbers)
# print(list(result))
# result = map(by_3, my_numbers)
# print(list(result))

#
# def get_multiplier_v2(n):
#     def multiplier(x):
#         return x * n
#     return multiplier
#
# by_5 = get_multiplier_v2(5)
# print(by_5(x=42))
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# by_10 = get_multiplier_v2(10)
# by_100 = get_multiplier_v2(100)
#
# print(list(map(by_10, my_numbers)))
# print(list(map(by_100, my_numbers)))


# from pprint import pprint
#
# def matrix(some_list):
#     def multyply_column(x):
#         res = []
#         for element in some_list:
#             res.append(element * x)
#         return res
#     return  multyply_column
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
#
# matrix_on_my_num = matrix(my_numbers)
#
# result = map(matrix_on_my_num, they_numbers)
# pprint(list(result))
#
# '''my_numbers.extend([10, 20, 30])
# result = map(matrix_on_my_num, they_numbers)
# pprint(list(result))'''


# Создание объекта, который можно вызвать
class Multilier:
    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        #если есть такой метод у класса - то его объект можно вызвать как функцию
        return x * self.n

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
by_100500 = Multilier(n=100500)
result = by_100500(x=42)
print(result)

result = map(by_100500,my_numbers)
print(list(result))