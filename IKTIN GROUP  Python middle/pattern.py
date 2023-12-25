

class Singleton(object):
    obj = None # единственный экземпляр класса

    def __new__(cls, *args, **kwargs):
    if cls.obj is None:
        cls.obj = object.__new__(cls, *args, **kwargs)
    return cls.obj

single = Singleton()
single.attr = 42
newSingle = Singleton()
newSingle.attr # 42
newSingle is single # true



Инкапсуляция
Все объекты в Python инкапсулируют внутри себя данные и методы работы с ними, предоставляя публичные интерфейсы для взаимодействия.

Атрибут может быть объявлен приватным (внутренним) с помощью нижнего подчеркивания перед именем, но настоящего скрытия на самом деле не происходит – все на уровне соглашений.


class SomeClass:
    def _private(self):
        print("Это внутренний метод объекта")

obj = SomeClass()
obj._private() # это внутренний метод объекта

Если поставить перед именем атрибута два подчеркивания, к нему нельзя будет обратиться напрямую. Но все равно остается обходной путь:

class SomeClass():
    def __init__(self):
        self.__param = 42 # защищенный атрибут

obj = SomeClass()
obj.__param # AttributeError: 'SomeClass' object has no attribute '__param'
obj._SomeClass__param # 42


Наследование
Язык программирования Python реализует как стандартное одиночное наследование:

