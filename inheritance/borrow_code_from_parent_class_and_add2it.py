# borrow_code_from_parent_class_and_add2it.py
from inherit import Parent, Parent2

class Child1(Parent):
    def yow(self):    # add new method
        print('Child1.yow')


class Child2(Parent):
    def spam(self):    # redefine a method in Parent
        print('Child2.spam', self.value)


class Child3(Parent):
    def spam(eslf):    # wrapper around the original
        print('Child3.spam')    # minor tweak, minor enhancement
        super().spam()    # Invokes the original spam() method


class Child4(Parent):
    def __init__(self, value, extra):    # Add new attr
        self.extra = extra
        super().__init__(value)    # Initialize parent also


class Child5(Parent, Parent2):    # Multiple inheritance
    pass


c1 = Child1(12)
print(c1.spam())
print(c1.grok())
print(c1.yow())

c2 = Child2(22)
print(c2.spam())
print(c2.grok())

c3 = Child3(32)
print(c3.spam())

c4 = Child4(42, 37)
print(c4.value)
print(c4.extra)

c5 = Child5(52)
print(c5.spam())
print(c5.grok())
print(c5.yow())