# # 1. Написать функцию, которая возвращает функцию повторения двух первых символов н-ное количество раз
# # 2. Создать массив функций и применять все функции поочередно к аргументу
# # 3. Применить все функции поочередно к массиву функций
#
# animal = 'мишка'
# animals = ['зайка', 'мишка', 'бегемотик']
#
#
# def gen_repeat(n):
#     def repeat(animal):
#         return (animal[
#                 :2] + '-') * n + animal  # берет первые два символа, плюсует тире и повторяет н раз и возвращаем параметр энимал
#
#     return repeat
#
#
# test_1 = gen_repeat(1)
# test_2 = gen_repeat(2)
#
# print(test_1(animal))
# print(test_2(animal))
#
# #2
#
# repetishions = [gen_repeat(n) for n in range(1, 4)] #всего будет 3 функции
# print(repetishions)
#
# result = [func(animal) for func in repetishions]#вызываем ф-ю фанк к переменной энимал
# print(result)
#
#
# #3 нужно что все 3 сгенерированные функции применились к списку энималс
# fin_result = [func(x) for func in repetishions for x in animals]
# print(fin_result)


# Задача - есть функция, которая возвращает результат введения числа а в степень б
# Нужно ускорить ее, чтобы она не делала повторные вычисления

def memoize_func(f):
    mem = {}

    def wrapper(*args):
        print(f'Выполнение функции с аргументами={args}, внутренняя память - {mem}')
        if args not in mem:
            mem[args] = f(*args)
            return f"функция выполнилась, ответ = {mem[args]}"
        else:
            return f"функция уже была выполнена раньше, ответ = {mem[args]}"

    return wrapper

@memoize_func
def func(a, b):
    print(f'Выполняем функцию с аргументами {a}, {b}')
    return a ** b


print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 2), '\n')
print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')
