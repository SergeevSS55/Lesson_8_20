# def f1(number):
#     return 10/number
# def f2():
#     print('Какой хороший день!')
#     result_f1 = f1(0)
#     return result_f1
# try:
#     total = f2()
#     print(total)
# except ZeroDivisionError as exc:
#     print(f'вот что пошло не так - {exc}')

# def f1(number):
#     return 10/number
# def f2():
#     print('Какой хороший день!')
#     summ = 0
#     for i in range(-2, 2):
#         summ += f1(i)
#         print(summ)
#     return summ
# try:
#     total = f2()
#     print(total)
# except ZeroDivisionError as exc:
#     print(f'вот что пошло не так - {exc}')

# def f1(number):
#     return 10/number
# def f2():
#     print('Какой хороший день!')
#     summ = 0
#     for i in range(-2, 2, 1):
#         try:
#             summ += f1(i)
#             print(summ)
#         except ZeroDivisionError as exc:
#             print(f'внутри f1 что-то пошло не так: {exc}')
#     return summ/0
# try:
#     total = f2()
#     print(f'результат функции: {total}')
# except ZeroDivisionError as exc:
#     print(f'внутри f2 что-то пошло не так: {exc}')

def f1(number):
    return total/number
def f2():
    try:
        result_f1 = f1(0)
        print(result_f1)
    except ZeroDivisionError as exc:
        print(f'внутри f1 что-то пошло не так: {exc}')
    return result_f1/0
try:
    f2()
# except ZeroDivisionError as exc:
except NameError as exc:
    print(f'внутри f2 что-то пошло не так: {exc}')