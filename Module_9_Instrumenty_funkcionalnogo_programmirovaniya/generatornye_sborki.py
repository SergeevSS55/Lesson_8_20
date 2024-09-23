# ленивые вычисления - это когда значения вычисляются при необходимости ( а не сразу, когда мы записываем)
# Это делают генераторы
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# result = (x ** 10 for x in my_numbers)
# print(result)
#
# for elem in result:
#     print(elem)


# Прочитать генераторную сборку можно лишь один раз
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# result = (x ** 10 for x in my_numbers)
# print(result)
#
# for elem in result:
#     print(elem)
#
# print('Еще разок')
#
# for elem in result:
#     print(elem)


# Используется там, где надо производить затратные операции
# import time
#
# start_time = time.time()
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# result = (x ** 1000 for x in my_numbers)
# print(result)
#
# for elem in result:
#     print(elem)
#
# finish_time = time.time()
# print(f'Время в милисекундах: {(finish_time - start_time) * 1000}')


# Демонстрация встроенных функций с ленивыми вычислениями

list_1 = [1, 5, 9, 29, 4]
list_2 = [5, 9, 2, 1, 2]

ran = range(10, 30)
zp = zip(list_1, list_2)
mp = map (str, list_1)

print(ran, zp, mp)
print(list(ran))
print(list(zp))
print(list(mp))