# best_food4the_month_01.py

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
    if (month.lower().endswith('r') or
        month.lower().endswith('ary')):
        print('%s: oysters' % month)
    elif 8 > MONTHS.index(month) > 4:
        print('%s: tomatoes' % month)
    else:
        print('%s: asparagus' % month)

if __name__ == '__main__':
    what_to_eat('November')
    what_to_eat('July')
    what_to_eat('March')
