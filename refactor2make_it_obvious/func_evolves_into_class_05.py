# func_evolves_into_class_05.py

MONTHS = ('January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December')

# Extract variables into classes to
# improve testability
class OystersGood:
    def __init__(self, month):
        lowered = month.lower()
        self.r = lowered.endswith('r')
        self.ary = lowered.endswith('ary')
        self._result = self.r or self.ary

    # Use __bool__ to indicate a class is a
    # paper trail  
    def __bool__(self): # aka __nonzero__
        return self._result


class TomatoesGood:
    def __init__(self, month):
        self.index = MONTHS.index(month)
        self._result = 8 > self.index > 4

    # Use __bool__ to indicate a class is a
    # paper trail
    def __bool__(self): # aka __nonzero__
        return self._result



def what_to_eat(month):
    time_for_oysters = OystersGood(month)
    time_for_tomatoes = TomatoesGood(month)
    if time_for_oysters:
        print('%s: oysters' % month)
    elif time_for_tomatoes:
        print('%s: tomatoes' % month)
    else:
        print('%s: asparagus' % month)


if __name__ == '__main__':
    what_to_eat('November')
    what_to_eat('July')
    what_to_eat('March')