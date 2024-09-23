import requests
from pprint import pprint


# help(requests)

class SomeClass:
    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)


some_object = SomeClass()

attr_name = 'attribute_2'

print(hasattr(some_object, attr_name))  # False
print(hasattr(some_object, 'attribute_1'))  # True
print(getattr(some_object, 'attribute_1'))  # 27
print(getattr(some_object, attr_name, 'Этого атрибута нет!'))
# pprint(dir(some_object))

for attr_name in dir(requests):
    attr = getattr(requests, attr_name)
    print(attr_name, type(attr))