# hot_swap.py

class Spam(object):
    def __init__(self, magicnum):
        self.magicnum = magicnum

    def func01(self):
        return self.magicnum

    def func42(self):
        return 42

spam = Spam(11)
print(spam.func01())
print(spam.func42())

spam.func01 = spam.func42
print(spam.func01())
