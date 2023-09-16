from abc import ABCMeta,abstractmethod
class Programming(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):
        pass

class Python(Programming):
    def has_oop(self):
        return "yes"

p1 = Python()
p2 = Programming()
print(p1.has_oop())
# print(p2.has_oop())

