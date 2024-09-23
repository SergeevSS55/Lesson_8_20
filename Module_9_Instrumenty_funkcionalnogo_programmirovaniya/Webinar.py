# list_ = [1, 2, 3]
# it = iter(list_)
# print(it) #<list_iterator object at 0x000001E062C51660>
# print(next(it)) # 1 принцип работы for только вручную
# print(next(it)) # 2
# print(next(it)) # 3
# for i in list_:
#     print(i)


# class OwnIterator:
#     def __init__(self, end):
#         self.end = end
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.counter < self.end:
#             self.counter += 1
#             return self.counter
#         else:
#             raise StopIteration
#
#
# a = OwnIterator(5)
#
# for i in a: # обязательное наличие метода __Итер__ в классе
#     print(i)

# class HumansIterator:
#     def __init__(self, group, end):
#         self.end = end
#         self.group = group
#         self.count = 0
#
#     def __next__(self):
#         if self.count < len(self.group):
#             first = self.group[self.count]
#             self.count += 1
#             return first
#         else:
#             raise StopIteration
#
#
# class Humans:
#     def __init__(self, group):
#         self.group = group
#         self.counter = 0
#
#     def __iter__(self):
#         return HumansIterator(self.group, len(self.group))
#
#
# students = Humans(['Alice', 'Bob', 'Den', 'Anna'])
# # print(next(students)) #TypeError: 'Humans' object is not an iterator
# it = iter(students)
# print(next(it))
# print(next(it))
# for i in students:
#     print(i)


# def test_gen():
#     counter = 0
#     while True:
#         yield counter
#         counter += 1
#
#
# a = test_gen()
# for i in a:
#     print(i) #хранится только то значение, которое выводим в текущий момент
#

def hello_upgrade(func):
    def wrapper(name): #можно (*args, **kwargs), если не знаем количество параметров из функции hello
        print('Before')
        res = func(name) #func(*args)
        print('After')
        return res ** 2  #возвращает результат из функции hello

    return wrapper


@hello_upgrade
def hello(name):
    print('Hello', name)
    return 5 + 5


print(hello(
    'Den'))  # None потому что за нее отвечает декоратор,
# чтобы изменить поведение ретерна, делаем ретерн во внутренней функции
