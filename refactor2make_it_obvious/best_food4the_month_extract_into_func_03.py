# best_food4the_month_extract_into_func_03.py

def oysters_good(month):
     lowered = month.lower()
     return (
         lowered.endswith('r') or
         lowered.endswith('ary'))

def tomatoes_good(month):
     index = MONTHS.index(month)
     return 8 > index > 4

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

def what_to_eat(month):
    if oysters_good(month):
        print('%s: oysters' % month)
    elif tomatoes_good(month):
        print('%s: tomatoes' % month)
    else:
        print('%s: asparagus' % month)


if __name__ == '__main__':
    what_to_eat('November')
    what_to_eat('July')
    what_to_eat('March')