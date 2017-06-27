# combine_extract_vars_with_func_04.py

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

def oysters_good(month):
     lowered = month.lower()
     return (
         lowered.endswith('r') or
         lowered.endswith('ary'))

def tomatoes_good(month):
     index = MONTHS.index(month)
     return 8 > index > 4

def what_to_eat(month):
    time_for_oysters = oysters_good(month)
    time_for_tomatoes = tomatoes_good(month)
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