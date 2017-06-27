# best_food4the_month_extract_vars_02.py

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
    lowered = month.lower()
    ends_in_r = lowered.endswith('r')
    ends_in_ary = lowered.endswith('ary')
    index = MONTHS.index(month)
    summer = 8 > index > 4
    
    if ends_in_r or ends_in_ary:
        print('%s: oysters' % month)
    elif summer:
        print('%s: tomatoes' % month)
    else:
        print('%s: asparagus' % month)


if __name__ == '__main__':
    what_to_eat('November')
    what_to_eat('July')
    what_to_eat('March')
