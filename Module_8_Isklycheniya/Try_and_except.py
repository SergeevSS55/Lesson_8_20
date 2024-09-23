# try:
#     <пишем код с возможной ошибкой>
# except:
#     <пишем блок кода в случае возниконовения ошибки>
# try:
#     i = 0
#     print(10 / i)
#     print('Cделано')
# except ZeroDivisionError: #указываем название класса ошибки
#     print('Hа ноль делить нельзя')

# try:
#     c = a + b
#     c = 10 / 0
# except (ZeroDivisionError, NameError):
#     print('Что-то пошло не так, но мы устояли')

# try:
#     c = a + b
#     c = 10 / 0
# except ZeroDivisionError:
#     print("На ноль делить нельзя")
# except NameError:
#     print('Нет такой перменной')

# try:
#     a = 10/0
# except ZeroDivisionError as exc:
#     print(f"вот что пошло не так - {exc}")

# try:
#     file = open("Tekst.txt") #такого файла нет в директории
# except OSError as exc:
#     print(f'вот что пошло не так - {exc} параметры {exc.args}')
try:
    i = int(input('Введите число: '))
    try:
        result = 10 * (1/i)
    except ZeroDivisionError as exc:
        print('Нельзя делить на ноль', exc)
    else:
        print('Ура, мы не делим на ноль')
    finally:
        print('Файнали мы заканчиваем урок')
except:
    print('Введите число!')

