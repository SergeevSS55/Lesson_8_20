# def greet_person(person_name):
#     if person_name == 'ВоланДеМорт':
#         raise Exception ("Мы не любим тебя, ВоланДеМорт")
#     print(f'Hello {person_name}')
#
#
# greet_person('Дорогой ученик')
# greet_person('ВоланДеМорт')

# try:
#     raise NameError('Привет Там')
# except NameError as exc:
#     print(f"Исключение типа {type(exc)}, его параметры {exc.args}")
#     raise

class ProZero(Exception):
    pass

def f(a, b):
    if b == 0:
        raise ProZero('Деление на ноль невозможно')
    return a/b

print(f(5, 1))
print(f(5, 0))