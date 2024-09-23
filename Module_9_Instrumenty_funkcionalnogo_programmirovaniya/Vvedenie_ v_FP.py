# пример 1 - почему функция - это объект

# def get_russians_names():
#     print(['Коля', 'Ваня', 'Маша', ])
#
# get_russians_names()
#
# # print(type(get_russians_names))
# print(get_russians_names.__name__)
# print(type(get_russians_names()))

# с функцией можно работать как с обычными объектами

# def get_russians_names():
#     return ['Коля', 'Ваня', 'Маша', ]
#
# def get_british_names():
#     return ['Oliver', 'Jack', 'Harry', ]
#
# get_names = [get_russians_names, get_british_names]
#
# for get_name in get_names:
#     print(get_name())


# def adder(args):
#     res = 0
#     for number in args:
#         res += number
#     return res
#
# def multiplier(args):
#     res = 1
#     for number in args:
#         res *= number
#     return res
#
# def process_numbers(numbers, functions):
#     result = functions(numbers)
#     print(f'Получилось {result}')
#
# my_nubers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# process_numbers(numbers=my_nubers, functions=adder)
# process_numbers(numbers=my_nubers, functions=multiplier)


# map применяет функцию к каждому элементу последовательности и формирует список результатов

# def mul_by_2(x):
#     return x * 2
#
# my_nubers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# result = map(mul_by_2, my_nubers)
# print(result)
# print(list(result))


def is_odd(x):
    return x % 2

my_nubers = [3, 1, 4, 1, 5, 9, 2, 6]

result = filter(is_odd, my_nubers)
print(result)
print(list(result))