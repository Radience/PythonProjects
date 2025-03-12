import abc
from abc import ABC, abstractmethod

class parent(ABC):
    @abstractmethod
    def someMethod(self):
        return "parent class"

class child(parent):
    def someMethod(self):
        return "child class"

obj = child()
print(obj.someMethod())
