# import time
# import sys
#
#
# def func_gen_dec(precision):
#     def dec(func):
#         def wrapper(*args, **kwargs):
#             started_at = time.time()
#             result = func(*args, **kwargs)
#             ended_at = time.time()
#             elapsed = round(ended_at - started_at, precision)
#             print(f'Функция работала {elapsed} секунд(ы)')
#             return result
#
#         return wrapper
#
#     return dec
#
#
# def digits(*args):
#     total = 1
#     for number in args:
#         total *= number ** 5000
#     return len(str(total))
#
#
# sys.set_int_max_str_digits(10 ** 5)
#
# time_track_precision_6 = func_gen_dec(precision=2)
# digits = time_track_precision_6(digits)
# result = digits(3141, 5926, 2718, 2818)
# print(result)


# # пример №2 синтаксический сахар поможет сделать все копмактно
# import time
# import sys
#
#
# def func_gen_dec(precision):
#     def dec(func):
#         def wrapper(*args, **kwargs):
#             started_at = time.time()
#             result = func(*args, **kwargs)
#             ended_at = time.time()
#             elapsed = round(ended_at - started_at, precision)
#             print(f'Функция работала {elapsed} секунд(ы)')
#             return result
#
#         return wrapper
#
#     return dec
#
#
# @func_gen_dec(precision=6)
# def digits(*args):
#     total = 1
#     for number in args:
#         total *= number ** 5000
#     return len(str(total))
#
#
# sys.set_int_max_str_digits(10 ** 5)
#
# result = digits(3141, 5926, 2718, 2818)
# print(result)



# Пример 3 - более подробное объяснение
import time
import sys


def func_gen_dec(precision):
    print("получили точность, с которой надо выводить результат")
    print("начинаем создавать декоратор")
    def dec(func):
        print(f"декоратор принял на вход функцию, которую надо отредактировать - {func}")
        print('начинаем создавать функцию-обертку')
        def wrapper(*args, **kwargs):
            print("мы в функции-обертке, которая заместит реальную функцию func")
            print("засекаем время")
            started_at = time.time()
            print("запускаем реальную функцию с переданными в функцию-обертку параметрами и запоминаем результат")
            result = func(*args, **kwargs)
            print("определяем затраченное время и выводим его")
            ended_at = time.time()
            print(f"вот тут и пригодится precision (== {precision}) - он запомнился в замыкании surrogate")
            elapsed = round(ended_at - started_at, precision)
            print(f'Функция работала {elapsed} секунд(ы)')
            print("возвращаем результат, который вернула реальная функция")
            return result
        print("декорат ор создал функцию-обертку и возвращает ее")
        return wrapper
    print("декоратор создан и его пора вернуть")
    return dec

@func_gen_dec(precision=6)
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


sys.set_int_max_str_digits(10 ** 5)

result = digits(3141, 5926, 2718, 2818)
print(result)
