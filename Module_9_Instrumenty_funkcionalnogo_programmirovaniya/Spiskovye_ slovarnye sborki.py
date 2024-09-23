# def by_3(x):
#     return x * 3
#
# def is_odd(x):
#     return x % 2
#
# my_nubers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# result = map(by_3, filter(is_odd, my_nubers))
# print(result)
# print(list(result))


# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# result = [x * 3 for x in my_numbers]
# print(result)
#
# фильтрация данных
# result1 = [x * 3 for x in my_numbers if x % 2] #эта строчка заменила полностью код с 1 по 11 строку
# print(result1)

# условие перед циклом, чтоб не отфильтровать данные, а поменять операцию над ними
# my_numb = ['A', 1, 4, '8', 5, 'C', 2, 6]
# result = [x if type(x) == str else x * 5 for x in my_numb]
# print(result)


# вложенные списки (генерация для двух элементов)
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
# they_numbers = [2, 7, 1, 8, 2, 8, 1, 8]
#
# result = [x * y for x in my_numbers for y in they_numbers]
# print(result)
#
# result = [x * y for x in my_numbers for y in they_numbers if x % 2]
# print(result)
#
# result = [x * y for x in my_numbers for y in they_numbers if x % 2 and y // 5]
# print(result)


# можно создавать множества и словари
my_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 7, 7, 9, 2, 6, 1]
they_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

result = {x for x in my_numbers}
print(result)

result = {x: x ** 2 for x in they_numbers}
print(result)

res = [x for x in range(1, 15)]
print(res)
